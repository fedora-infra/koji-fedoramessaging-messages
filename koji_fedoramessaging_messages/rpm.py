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

from typing import List

from .base import KojiFedoraMessagingMessage, SCHEMA_URL


class SignV1(KojiFedoraMessagingMessage):
    """This message is sent when a rpm is signed."""

    topic = "buildsys.rpm.sign"

    body_schema = {
        "$id": f"{SCHEMA_URL}/v1/{topic}#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "An rpm build was signed by the build system.",
        "type": "object",
        "properties": {
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji",
            },
            "sigkey": {"type": "string", "description": "the signing key"},
            "rpm": {
                "type": "object",
                "description": "An rpm build",
                "properties": {
                    "build_id": {"type": "integer", "description": "koji build id"},
                    "name": {"type": "string", "description": "name of the rpm"},
                    "extra": {
                        "type": ["null", "string"],
                        "description": "extra",
                    },
                    "arch": {
                        "type": "string",
                        "description": "build architecture",
                    },
                    "buildtime": {
                        "type": "integer",
                        "description": "build timestamp",
                    },
                    "id": {
                        "type": "integer",
                        "description": "id",
                    },
                    "epoch": {
                        "type": ["null", "string", "integer"],
                        "description": "epoch",
                    },
                    "version": {
                        "type": "string",
                        "description": "rpm version",
                    },
                    "metadata_only": {
                        "type": "boolean",
                        "description": "metadata only",
                    },
                    "external_repo_id": {
                        "type": "integer",
                        "description": "external repo id",
                    },
                    "release": {
                        "type": "string",
                        "description": "rpm release number",
                    },
                    "size": {
                        "type": "integer",
                        "description": "size",
                    },
                    "buildroot_id": {
                        "type": "integer",
                        "description": "buildroot id",
                    },
                    "external_repo_name": {
                        "type": "string",
                        "description": "external_repo_name",
                    },
                    "payloadhash": {
                        "type": "string",
                        "description": "payload hash",
                    },
                },
            },
            "build": {
                "type": "object",
                "description": "build details",
                "properties": {
                    "cg_id": {
                        "type": ["null", "integer", "string"],
                        "description": "cg id",
                    },
                    "package_name": {
                        "type": "string",
                        "description": "package name",
                    },
                    "extra": {
                        "type": "object",
                        "description": "extra",
                        "properties": {
                            "source": {
                                "type": "object",
                                "description": "build source",
                                "properties": {
                                    "original_url": {
                                        "type": "string",
                                        "description": "dist git url",
                                    },
                                },
                            },
                        },
                    },
                    "creation_time": {
                        "type": "number",
                        "description": "koji build creation time",
                    },
                    "completion_time": {
                        "type": "number",
                        "description": "koji build completion time",
                    },
                    "package_id": {
                        "type": "integer",
                        "description": "package id",
                    },
                    "cg_name": {
                        "type": ["null", "integer", "string"],
                        "description": "cg name",
                    },
                    "id": {
                        "type": "integer",
                        "description": "id",
                    },
                    "build_id": {
                        "type": "integer",
                        "description": "build id",
                    },
                    "epoch": {
                        "type": ["null", "integer", "string"],
                        "description": "epoch",
                    },
                    "source": {
                        "type": "string",
                        "description": "dist git url",
                    },
                    "state": {
                        "type": "integer",
                        "description": "koji build state",
                    },
                    "version": {
                        "type": "string",
                        "description": "rpm version",
                    },
                    "owner_id": {
                        "type": "integer",
                        "description": "owner id",
                    },
                    "owner_name": {
                        "type": "string",
                        "description": "owner name",
                    },
                    "nvr": {
                        "type": "string",
                        "description": "rpm name version release",
                    },
                    "start_time": {
                        "type": "integer",
                        "description": "build start time",
                    },
                    "creation_event_id": {
                        "type": "integer",
                        "description": "creation event id",
                    },
                    "volume_id": {
                        "type": "integer",
                        "description": "volume id",
                    },
                    "creation_ts": {
                        "type": "number",
                        "description": "creation timestamp",
                    },
                    "name": {
                        "type": "string",
                        "description": "name",   # That's not a very informative description
                    },
                    "task_id": {
                        "type": "integer",
                        "description": "koji task id",
                    },
                    "volume_name": {
                        "type": "string",
                        "description": "volume name",
                    },
                    "release": {
                        "type": "string",
                        "description": "rpm release number",
                    },
                },
            },
            "sighash": {
                "type": "string",
                "description": "signing hash",
            },
        },
    }

    @property
    def owner(self):
        try:
            return self.body["build"]["owner_name"]
        except KeyError:
            return None

    @property
    def instance(self) -> str:
        return self.body.get("instance")

    @property
    def sigkey(self) -> str:
        return self.body.get("sigkey")

    @property
    def rpm(self) -> dict:
        return self.body.get("rpm")

    @property
    def build(self) -> dict:
        return self.body.get("build")

    @property
    def sighash(self) -> str:
        return self.body.get("sighash")

    @property
    def name(self):
        try:
            return self.body["build"]["name"]
        except KeyError:
            return None

    @property
    def agent_name(self) -> str:
        # It seems safe to assume that the build owner is also the initiator of the signing action.
        return self.owner

    @property
    def summary(self) -> str:
        return f"rpm build {self.body.get('build', dict()).get('nvr')} was signed"

    @property
    def packages(self):
        return [self.name] if self.name else []
