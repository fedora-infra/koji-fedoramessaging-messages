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


from .base import KojiFedoraMessagingMessage, SCHEMA_URL

TAG = {
    "type": "object",
    "properties": {
        "build_id": {"type": "integer", "description": "build id"},
        "name": {"type": "string", "description": "package name"},
        "tag_id": {
            "type": "integer",
            "description": "tag id",
        },
        "instance": {
            "type": "string",
            "description": "distinguish between messages from primary and secondary koji",
        },
        "tag": {
            "type": "string",
            "description": "name of the tag",
        },
        "user": {
            "type": "string",
            "description": "name of the user that trigger the build",
        },
        "version": {
            "type": "string",
            "description": "version of the build",
        },
        "owner": {
            "type": "string",
            "description": "name of the package owner",
        },
        "release": {
            "type": "string",
            "description": "release number of the package",
        },
    },
}


class TagMessage(KojiFedoraMessagingMessage):
    @property
    def build_id(self) -> int:
        return self.body.get("build_id")

    @property
    def name(self) -> str:
        return self.body.get("name")

    @property
    def tag_id(self) -> int:
        return self.body.get("tag_id")

    @property
    def instance(self) -> str:
        return self.body.get("instance")

    @property
    def tag(self) -> str:
        return self.body.get("tag")

    @property
    def user(self) -> str:
        return self.body.get("user")

    @property
    def version(self) -> str:
        return self.body.get("version")

    @property
    def owner(self) -> str:
        return self.body.get("owner")

    @property
    def release(self) -> str:
        return self.body.get("release")

    @property
    def summary(self) -> str:
        return f"{self.name}-{self.version}-{self.release} was {self._summary_action} {self.tag}"

    @property
    def packages(self):
        return [self.name]


class TagV1(TagMessage):
    """This message is sent when a package is tagged."""

    topic = "buildsys.tag"
    _summary_action = "tagged into"
    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package is tagged.",
        "type": "object",
        "properties": TAG,
    }


class UntagV1(TagMessage):
    """This message is sent when a package is untagged."""

    topic = "buildsys.untag"
    _summary_action = "untagged from"
    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package is untagged.",
        "type": "object",
        "properties": TAG,
    }
