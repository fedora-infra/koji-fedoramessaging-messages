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

import re
from typing import List

from fedora_messaging.message import DEBUG

from .base import SCHEMA_URL, KojiFedoraMessagingMessage

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

_MASS_REBUILD_RE = re.compile(r"^f\d+-rebuild$")
_ELN_RE = re.compile(r"^eln(-.*)?$")


class TagMessage(KojiFedoraMessagingMessage):
    severity = DEBUG

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.priority = self._choose_priority()

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
        return (
            f"{self.name}-{self.version}-{self.release} was {self._summary_action}"
            f" {self.tag} by {self.user}"
        )

    @property
    def packages(self) -> List[str]:
        return [self.name] if self.name else []

    @property
    def agent_name(self) -> str:
        # This looks like it's the action initiator, no? Seems more correct than the owner.
        return self.user

    @property
    def usernames(self) -> List[str]:
        return [name for name in (self.agent_name, self.owner) if name is not None]

    @property
    def is_mass_rebuild(self) -> bool:
        return self.tag and _MASS_REBUILD_RE.match(self.tag) is not None

    @property
    def is_eln(self) -> bool:
        return self.tag and _ELN_RE.match(self.tag) is not None

    def _choose_priority(self) -> int:
        # https://pagure.io/fedora-infrastructure/issue/10899
        if self.is_mass_rebuild:
            return 0
        if self.is_eln:
            return 1
        return 2


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
