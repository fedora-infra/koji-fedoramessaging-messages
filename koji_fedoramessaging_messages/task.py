# SPDX-FileCopyrightText: 2020-2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Define schema for fedora messages sent by koji"""

import logging

from .base import SCHEMA_URL, TASK_INFO, KojiFedoraMessagingMessage
from .utilities import fill_task_template

log = logging.getLogger(__name__)


class TaskStateChangeV1(KojiFedoraMessagingMessage):
    """This message is sent when a task state changes."""

    topic = "buildsys.task.state.change"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$defs": {
            "task_info": TASK_INFO,
        },
        "description": "A koji task state changed.",
        "type": "object",
        "properties": {
            "info": {"$ref": "#/$defs/task_info"},
            "id": {"$ref": "#/$defs/task_info/properties/id"},
            "method": {"$ref": "#/$defs/task_info/properties/method"},
            "attribute": {
                "type": "string",
                "description": "the attribute that changed. Always 'state'.",
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji",
            },
            "owner": {
                "type": ["string", "null"],
                "description": "name of the package owner",
            },
            "srpm": {
                "type": "string",
                "description": "the source rpm in the request",
            },
            # URLs
            "base_url": {
                "type": "string",
                "description": "The base URL of the koji instance",
            },
            "files_base_url": {
                "type": "string",
                "description": "The base URL where the result files are hosted",
            },
            # States
            "old": {
                "type": ["string", "null"],
                "description": "previous task state",
            },
            "new": {
                "type": "string",
                "description": "name of the new task state",
            },
        },
        "required": [
            "id",
            "info",
            "method",
            "attribute",
            "old",
            "new",
            "srpm",
            "owner",
            "base_url",
            "files_base_url",
            "instance",
        ],
    }

    @property
    def info(self) -> dict:
        return self.body["info"]

    @property
    def old(self) -> str:
        return self.body["old"]

    @property
    def attribute(self) -> str:
        return self.body["attribute"]

    @property
    def task_id(self) -> int:
        return self.body["id"]

    @property
    def instance(self) -> str:
        return self.body["instance"]

    @property
    def owner(self) -> str:
        return self.body["owner"]

    @property
    def agent_name(self) -> str:
        return self.owner

    @property
    def new(self) -> str:
        return self.body["new"]

    @property
    def srpm(self) -> str:
        return self.body["srpm"]

    @property
    def arch(self) -> str:
        return self.info["arch"]

    @property
    def method(self) -> str:
        return self.body["method"]

    @property
    def url(self) -> str:
        return self.body["info"]["url"]

    @property
    def summary(self):
        return f"Task {self.new} -- {self.method or ''} ({self.srpm or ''} {self.arch or ''})"

    def __str__(self) -> str:
        return fill_task_template(self.body["info"], self.body["files_base_url"])
