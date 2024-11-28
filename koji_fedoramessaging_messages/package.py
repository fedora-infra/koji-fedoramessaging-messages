# SPDX-FileCopyrightText: 2020-2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Define schema for fedora messages sent by koji"""
from typing import Optional

from fedora_messaging.message import DEBUG

from .base import SCHEMA_URL, KojiFedoraMessagingMessage


class ListChangeV1(KojiFedoraMessagingMessage):
    """This message is sent when a package list changes."""

    topic = "buildsys.package.list.change"
    severity = DEBUG

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
        return self.body.get("force")

    @property
    def instance(self) -> str:
        return self.body.get("instance")

    @property
    def extra_arches(self) -> Optional[str]:
        return self.body.get("extra_arches")

    @property
    def package(self) -> str:
        return self.body.get("package")

    @property
    def update(self) -> Optional[bool]:
        return self.body.get("update")

    @property
    def owner(self) -> Optional[str]:
        return self.body.get("owner")

    @property
    def agent_name(self) -> Optional[str]:
        return self.owner  # is this action always done by the package owner? This seems incorrect.

    @property
    def tag(self) -> str:
        return self.body.get("tag")

    @property
    def action(self) -> str:
        return self.body.get("action")

    @property
    def block(self) -> Optional[bool]:
        return self.body.get("block")

    @property
    def summary(self):
        return f"Package list change for {self.package}:  {self.tag}"

    @property
    def packages(self) -> list[str]:
        return [self.package] if self.package else []
