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
from enum import Enum
from typing import List, Optional, Any

from .base import KojiFedoraMessagingMessage, SCHEMA_URL


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
        "description": "The state of the build changed.",
        "type": "object",
        "properties": {
            "build_id": {"type": ["null", "integer"], "description": "build id"},
            "old": {"type": "integer", "description": "previous state"},
            "name": {
                "type": "string",
                "description": "name of the package built",
            },
            "task_id": {
                "type": ["null", "integer"],
                "description": "task id",
            },
            "attribute": {
                "type": "string",
                "description": "attribute",
            },
            "request": {
                "type": ["null", "array"],
                "description": "build request details",
                "contains": {"type": "string"},
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji",
            },
            "epoch": {
                "type": ["null", "string", "integer"],
                "description": "epoch",
            },
            "version": {
                "type": "string",
                "description": "version of the build",
            },
            "owner": {
                "type": ["null", "integer", "string"],
                "description": "the owner of the build",
            },
            "new": {
                "type": "integer",
                "description": "new state",
            },
            "release": {
                "type": "string",
                "description": "release number of the package",
            },
        },
    }

    @property
    def build_id(self) -> Optional[int]:
        return self.body.get("build_id")

    @property
    def old(self) -> int:
        return self.body.get("old")

    @property
    def name(self) -> str:
        return self.body.get("name")

    @property
    def task_id(self) -> Optional[int]:
        return self.body.get("task_id")

    @property
    def attribute(self) -> str:
        return self.body.get("attribute")

    @property
    def request(self) -> Optional[List]:
        return self.body["request"]

    @property
    def instance(self) -> str:
        return self.body["instance"]

    @property
    def version(self) -> str:
        return self.body["version"]

    @property
    def owner(self) -> str:
        return self.body.get("owner")

    @property
    def new(self) -> int:
        return self.body["new"]

    @property
    def release(self) -> str:
        return self.body["release"]

    @property
    def epoch(self) -> Any:
        return self.body["epoch"]

    @property
    def agent_name(self) -> str:
        return self.owner

    @property
    def summary(self):
        return (
            f"Build {BUILD_STATES(self.new).name}: {self.owner}'s "
            f"{self.name}-{self.version}-{self.release}"
        )

    @property
    def packages(self) -> List[str]:
        return [self.name] if self.name else []
