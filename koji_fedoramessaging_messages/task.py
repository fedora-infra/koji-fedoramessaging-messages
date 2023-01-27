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


class TaskStateChangeV1(KojiFedoraMessagingMessage):
    """This message is sent when a task state changes."""

    topic = "buildsys.task.state.change"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A koji task state changed.",
        "type": "object",
        "properties": {
            "info": {
                "type": "object",
                "description": "task info",
                "properties": {
                    "parent": {
                        "type": ["null", "array"],
                        "description": "parent tasks",
                    },
                    "completion_time": {
                        "type": "number",
                        "description": "completion time",
                    },
                    "start_time": {
                        "type": "number",
                        "description": "start time",
                    },
                    "request": {
                        "type": ["null", "array"],
                        "description": "task request details",
                        "contains": {"type": "string"},
                    },
                    "waiting": {
                        "type": "boolean",
                        "description": "Is the task waiting or not",
                    },
                    "awaited": {
                        "type": "null",
                        "description": "awaited",
                    },
                    "id": {
                        "type": "integer",
                        "description": "id",
                    },
                    "priority": {
                        "type": "integer",
                        "description": "priority",
                    },
                    "channel_id": {
                        "type": "integer",
                        "description": "channel_id",
                    },
                    "state": {
                        "type": "integer",
                        "description": "task state",
                    },
                    "create_time": {
                        "type": "number",
                        "description": "create time",
                    },
                    "result": {
                        "type": "null",
                        "description": "result",
                    },
                    "owner": {
                        "type": ["null", "string", "integer"],
                        "description": "owner name or id",
                    },
                    "host_id": {
                        "type": "integer",
                        "description": "host id",
                    },
                    "method": {
                        "type": "string",
                        "description": "task method",
                    },
                    "label": {
                        "type": "null",
                        "description": "label",
                    },
                    "arch": {
                        "type": "string",
                        "description": "task specific architecture",
                    },
                    "children": {
                        "type": ["null", "array"],
                        "description": "task childrens",
                    },
                },
            },
            "old": {
                "type": "string",
                "description": "previous task state",
            },
            "attribute": {"type": "string", "description": "attribute"},
            "id": {
                "type": "integer",
                "description": "task id",
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji",
            },
            "owner": {
                "type": "string",
                "description": "name of the package owner",
            },
            "new": {
                "type": "string",
                "description": "name of the new task state",
            },
            "srpm": {
                "type": "string",
                "description": "name of the source rpm",
            },
            "method": {"type": "string", "description": "name of the task method"},
        },
    }

    @property
    def info(self) -> dict:
        return self.body.get("info")

    @property
    def old(self) -> str:
        return self.body.get("old")

    @property
    def attribute(self) -> str:
        return self.body.get("attribute")

    @property
    def id(self) -> int:
        return self.body.get("id")

    @property
    def instance(self) -> str:
        return self.body.get("instance")

    @property
    def owner(self) -> str:
        return self.body.get("owner")

    @property
    def new(self) -> str:
        return self.body.get("new")

    @property
    def srpm(self) -> str:
        return self.body.get("srpm")

    @property
    def arch(self) -> str:
        return self.info.get("arch")

    @property
    def method(self) -> str:
        return self.body.get("method")

    @property
    def summary(self):
        return f"Task {self.new} -- {self.method or ''} ({self.srpm or ''} {self.arch or ''})"
