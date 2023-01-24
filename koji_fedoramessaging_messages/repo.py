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


class DoneV1(KojiFedoraMessagingMessage):
    """This message is sent when a package repo is done."""

    topic = "buildsys.repo.done"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package repo task was done.",
        "type": "object",
        "properties": {
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji",
            },
            "repo_id": {"type": "integer", "description": "repo id"},
            "tag": {
                "type": "string",
                "description": "tag used to generate the repo",
            },
            "tag_id": {
                "type": "integer",
                "description": "tag id of the tag used to generate the repo",
            },
        },
    }

    @property
    def instance(self) -> str:
        return self.body["instance"]

    @property
    def repo_id(self) -> int:
        return self.body["repo_id"]

    @property
    def tag(self) -> str:
        return self.body["tag"]

    @property
    def tag_id(self) -> int:
        return self.body["tag_id"]


class InitV1(KojiFedoraMessagingMessage):
    """This message is sent when a package repo is initialized."""

    topic = "buildsys.repo.init"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package repo task is initialized.",
        "type": "object",
        "properties": {
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji.",
            },
            "repo_id": {"type": "integer", "description": "repo id"},
            "tag": {
                "type": "string",
                "description": "tag used to generate the repo",
            },
            "tag_id": {
                "type": "integer",
                "description": "tag id of the tag used to generate the repo",
            },
        },
    }

    @property
    def instance(self) -> str:
        return self.body["instance"]

    @property
    def repo_id(self) -> int:
        return self.body["repo_id"]

    @property
    def tag(self) -> str:
        return self.body["tag"]

    @property
    def tag_id(self) -> int:
        return self.body["tag_id"]
