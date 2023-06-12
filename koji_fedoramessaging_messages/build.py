# Copyright © 2020 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Define schema for fedora messages sent by koji"""

import logging
from enum import Enum
from typing import Optional

from .base import SCHEMA_URL, TASK_INFO, KojiFedoraMessagingMessage
from .utilities import date_to_string, fill_task_template

log = logging.getLogger(__name__)


# This enums is defined in
# https://pagure.io/koji/blob/master/f/koji/__init__.py
# But we need it here as the messages we get from the
# koji plugin only gives us the ints -- so we need to decode
# for summaries
class BUILD_STATES(Enum):
    BUILDING = 0
    COMPLETE = 1
    DELETED = 2
    FAILED = 3
    CANCELED = 4


class BuildStateChangeV1(KojiFedoraMessagingMessage):
    """This message is sent when a build state changes."""

    topic = "buildsys.build.state.change"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$defs": {
            "task_info": TASK_INFO,
        },
        "description": "The state of the build changed.",
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "name of the package built",
            },
            "version": {
                "type": "string",
                "description": "version of the build",
            },
            "release": {
                "type": "string",
                "description": "release number of the package",
            },
            "epoch": {
                "type": ["null", "string", "integer"],
                "description": "epoch",
            },
            "attribute": {
                "type": "string",
                "description": "attribute",
            },
            "build_id": {"type": ["null", "integer"], "description": "build id"},
            "owner": {
                "type": ["null", "string"],
                "description": "the owner of the build",
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji",
            },
            "url": {
                "type": ["null", "string"],
                "description": "the URL of the build in koji-web",
            },
            # Task
            "task_id": {
                "type": ["null", "integer"],
                "description": "task id",
            },
            "task": {
                "type": ["null", "object"],
                "desctiption": "the task that triggered this build, if any",
                "properties": {
                    "$ref": "#/$defs/task_info/properties",
                },
            },
            "request": {
                "description": "build request details",
                "type": ["array"],
            },
            # States
            "old": {"type": ["null", "integer"], "description": "previous state"},
            "new": {
                "type": "integer",
                "description": "new state",
            },
            # Timestamps
            "creation_time": {
                "type": "string",
                "description": "creation time in iso format",
            },
            "completion_time": {
                "type": ["string", "null"],
                "description": "completion time in iso format",
            },
        },
        "required": [
            "name",
            "version",
            "release",
            "epoch",
            "attribute",
            "old",
            "new",
            "build_id",
            "task_id",
            "task",
            "request",
            "owner",
            "instance",
            "creation_time",
            "completion_time",
        ],
    }

    @property
    def build_id(self) -> Optional[int]:
        return self.body["build_id"]

    @property
    def name(self) -> str:
        return self.body["name"]

    @property
    def task_id(self) -> Optional[int]:
        return self.body["task_id"]

    @property
    def attribute(self) -> str:
        return self.body["attribute"]

    @property
    def request(self) -> Optional[list]:
        return self.body["request"]

    @property
    def instance(self) -> str:
        return self.body["instance"]

    @property
    def version(self) -> str:
        return self.body["version"]

    @property
    def owner(self) -> Optional[str]:
        return self.body["owner"]

    @property
    def old(self) -> Optional[int]:
        return self.body["old"]

    @property
    def old_state_name(self) -> Optional[str]:
        return None if self.old is None else BUILD_STATES(self.old).name.lower()

    @property
    def new(self) -> int:
        return self.body["new"]

    @property
    def new_state_name(self) -> Optional[str]:
        return BUILD_STATES(self.new).name.lower()

    @property
    def release(self) -> str:
        return self.body["release"]

    @property
    def epoch(self) -> Optional[str | int]:
        return self.body["epoch"]

    @property
    def agent_name(self) -> Optional[str]:
        return self.owner

    @property
    def summary(self) -> str:
        return (
            f"Build {BUILD_STATES(self.new).name}: {self.owner}'s "
            f"{self.name}-{self.version}-{self.release}"
        )

    @property
    def packages(self) -> list[str]:
        return [self.name] if self.name else []

    @property
    def url(self) -> str:
        return self.body["url"]

    def __str__(self) -> str:
        _build_str = _build_template.format(
            name=self.name,
            version=self.version,
            release=self.release,
            status=self.new_state_name,
            owner_name=self.owner,
            id=self.build_id,
            started=date_to_string(self.body["creation_time"]),
            finished=date_to_string(self.body["completion_time"]),
        )
        if self.body["task"] is None:
            _task_str = "Build imported into koji\n"
        else:
            _task_str = "Closed tasks:\n-------------\n"
            _task_str += fill_task_template(self.body["task"], self.body["files_base_url"])

        return _build_str + _task_str


_build_template = """Package:    {name}-{version}-{release}
Status:     {status}
Built by:   {owner_name}
ID:         {id}
Started:    {started}
Finished:   {finished}

"""
