buildsys.rpm.sign
-----------------
::

    {
        "$id": "/v1/buildsys.rpm.sign#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "An rpm build was signed by the build system.",
        "type": "object",
        "properties": {
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji"
            },
            "sigkey": {
                "type": "string",
                "description": "the signing key"
            },
            "rpm": {
                "type": "object",
                "description": "An rpm build",
                "properties": {
                    "build_id": {
                        "type": "integer",
                        "description": "koji build id"
                    },
                    "name": {
                        "type": "string",
                        "description": "name of the rpm"
                    },
                    "extra": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "description": "extra"
                    },
                    "arch": {
                        "type": "string",
                        "description": "build architecture"
                    },
                    "buildtime": {
                        "type": "integer",
                        "description": "build timestamp"
                    },
                    "id": {
                        "type": "integer",
                        "description": "id"
                    },
                    "epoch": {
                        "type": [
                            "null",
                            "string",
                            "integer"
                        ],
                        "description": "epoch"
                    },
                    "version": {
                        "type": "string",
                        "description": "rpm version"
                    },
                    "metadata_only": {
                        "type": "boolean",
                        "description": "metadata only"
                    },
                    "external_repo_id": {
                        "type": "integer",
                        "description": "external repo id"
                    },
                    "release": {
                        "type": "string",
                        "description": "rpm release number"
                    },
                    "size": {
                        "type": "integer",
                        "description": "size"
                    },
                    "buildroot_id": {
                        "type": "integer",
                        "description": "buildroot id"
                    },
                    "external_repo_name": {
                        "type": "string",
                        "description": "external_repo_name"
                    },
                    "payloadhash": {
                        "type": "string",
                        "description": "payload hash"
                    }
                }
            },
            "build": {
                "type": "object",
                "description": "build details",
                "properties": {
                    "cg_id": {
                        "type": [
                            "null",
                            "integer",
                            "string"
                        ],
                        "description": "cg id"
                    },
                    "package_name": {
                        "type": "string",
                        "description": "package name"
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
                                        "description": "dist git url"
                                    }
                                }
                            }
                        }
                    },
                    "creation_time": {
                        "type": "number",
                        "description": "koji build creation time"
                    },
                    "completion_time": {
                        "type": "number",
                        "description": "koji build completion time"
                    },
                    "package_id": {
                        "type": "integer",
                        "description": "package id"
                    },
                    "cg_name": {
                        "type": [
                            "null",
                            "integer",
                            "string"
                        ],
                        "description": "cg name"
                    },
                    "id": {
                        "type": "integer",
                        "description": "id"
                    },
                    "build_id": {
                        "type": "integer",
                        "description": "build id"
                    },
                    "epoch": {
                        "type": [
                            "null",
                            "integer",
                            "string"
                        ],
                        "description": "epoch"
                    },
                    "source": {
                        "type": "string",
                        "description": "dist git url"
                    },
                    "state": {
                        "type": "integer",
                        "description": "koji build state"
                    },
                    "version": {
                        "type": "string",
                        "description": "rpm version"
                    },
                    "owner_id": {
                        "type": "integer",
                        "description": "owner id"
                    },
                    "owner_name": {
                        "type": "string",
                        "description": "owner name"
                    },
                    "nvr": {
                        "type": "string",
                        "description": "rpm name version release"
                    },
                    "start_time": {
                        "type": "integer",
                        "description": "build start time"
                    },
                    "creation_event_id": {
                        "type": "integer",
                        "description": "creation event id"
                    },
                    "volume_id": {
                        "type": "integer",
                        "description": "volume id"
                    },
                    "creation_ts": {
                        "type": "number",
                        "description": "creation timestamp"
                    },
                    "name": {
                        "type": "string",
                        "description": "name"
                    },
                    "task_id": {
                        "type": "integer",
                        "description": "koji task id"
                    },
                    "volume_name": {
                        "type": "string",
                        "description": "volume name"
                    },
                    "release": {
                        "type": "string",
                        "description": "rpm release number"
                    }
                }
            },
            "sighash": {
                "type": "string",
                "description": "signing hash"
            }
        }
    }

