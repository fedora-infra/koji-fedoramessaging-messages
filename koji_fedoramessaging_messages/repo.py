# SPDX-FileCopyrightText: 2020-2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Define schema for fedora messages sent by koji"""

from fedora_messaging.message import DEBUG

from .base import SCHEMA_URL, KojiFedoraMessagingMessage

REPO = {
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


class RepoMessage(KojiFedoraMessagingMessage):
    severity = DEBUG

    @property
    def instance(self) -> str:
        return self.body.get("instance")

    @property
    def repo_id(self) -> int:
        return self.body.get("repo_id")

    @property
    def tag(self) -> str:
        return self.body.get("tag")

    @property
    def tag_id(self) -> int:
        return self.body.get("tag_id")


class DoneV1(RepoMessage):
    """This message is sent when a package repo is done."""

    topic = "buildsys.repo.done"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package repo task was done.",
        "type": "object",
        "properties": REPO["properties"],
    }


class InitV1(RepoMessage):
    """This message is sent when a package repo is initialized."""

    topic = "buildsys.repo.init"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package repo task is initialized.",
        "type": "object",
        "properties": REPO["properties"],
    }
