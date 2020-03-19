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
from typing import List, Optional, Any

from fedora_messaging import message

SCHEMA_URL = "https://koji-fedmsg-plugin.readthedocs.io/en/latest/_schema"


class BuildStateChangeV1(message.Message):
    """ This message is sent when a build state changes. """

    topic = "buildsys.build.state.change"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "The state of the build changed.",
        "type": "object",
        "properties": {
            "build_id": {"type": ["null", "integer"], "description": "build id"},
            "old": {"type": "integer", "description": "previous state"},
            "name": {"type": "string", "description": "name of the package built",},
            "task_id": {"type": ["null", "integer"], "description": "task id",},
            "attribute": {"type": "string", "description": "attribute",},
            "request": {
                "type": ["null", "array"],
                "description": "build request details",
                "contains": {"type": "string"},
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji",
            },
            "epoch": {"type": ["null", "string", "integer"], "description": "epoch",},
            "version": {"type": "string", "description": "version of the build",},
            "owner": {
                "type": ["null", "integer", "string"],
                "description": "name of the package owner",
            },
            "new": {"type": "integer", "description": "new state",},
            "release": {"type": "string", "description": "release number of the package",},
        },
    }

    @property
    def build_id(self) -> Optional[int]:
        return self.body["build_id"]

    @property
    def old(self) -> int:
        return self.body["old"]

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
        return self.body["owner"]

    @property
    def new(self) -> int:
        return self.body["new"]

    @property
    def release(self) -> str:
        return self.body["release"]

    @property
    def epoch(self) -> Any:
        return self.body["epoch"]
