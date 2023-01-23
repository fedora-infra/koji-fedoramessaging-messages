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
from typing import Optional

from fedora_messaging import message

SCHEMA_URL = "https://koji-fedmsg-plugin.readthedocs.io/en/latest/_schema"


class ListChangeV1(message.Message):
    """This message is sent when a package list changes."""

    topic = "buildsys.package.list.change"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package list changed.",
        "type": "object",
        "properties": {
            "force": {"type": ["null", "boolean"], "description": "force"},
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji",
            },
            "extra_arches": {"type": ["null", "string"], "description": "extra arches"},
            "package": {
                "type": "string",
                "description": "name of the package updated",
            },
            "update": {
                "type": ["null", "boolean"],
                "description": "update",
            },
            "owner": {
                "type": ["null", "string"],
                "description": "name of the package owner",
            },
            "tag": {
                "type": "string",
                "description": "name of the tag",
            },
            "action": {
                "type": "string",
                "description": "name of the action",
            },
            "block": {"type": ["null", "boolean"], "description": "block"},
        },
    }

    @property
    def force(self) -> Optional[bool]:
        return self.body["force"]

    @property
    def instance(self) -> str:
        return self.body["instance"]

    @property
    def extra_arches(self) -> Optional[str]:
        return self.body["extra_arches"]

    @property
    def package(self) -> str:
        return self.body["package"]

    @property
    def update(self) -> Optional[bool]:
        return self.body["update"]

    @property
    def owner(self) -> Optional[str]:
        return self.body["owner"]

    @property
    def tag(self) -> str:
        return self.body["tag"]

    @property
    def action(self) -> str:
        return self.body["action"]

    @property
    def block(self) -> Optional[bool]:
        return self.body["block"]
