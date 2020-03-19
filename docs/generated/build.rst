buildsys.build.state.change
---------------------------
::

    {
        "$id": "/v1/buildsys.build.state.change#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "The state of the build changed.",
        "type": "object",
        "properties": {
            "build_id": {
                "type": [
                    "null",
                    "integer"
                ],
                "description": "build id"
            },
            "old": {
                "type": "integer",
                "description": "previous state"
            },
            "name": {
                "type": "string",
                "description": "name of the package built"
            },
            "task_id": {
                "type": [
                    "null",
                    "integer"
                ],
                "description": "task id"
            },
            "attribute": {
                "type": "string",
                "description": "attribute"
            },
            "request": {
                "type": [
                    "null",
                    "array"
                ],
                "description": "build request details",
                "contains": {
                    "type": "string"
                }
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji"
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
                "description": "version of the build"
            },
            "owner": {
                "type": [
                    "null",
                    "integer",
                    "string"
                ],
                "description": "name of the package owner"
            },
            "new": {
                "type": "integer",
                "description": "new state"
            },
            "release": {
                "type": "string",
                "description": "release number of the package"
            }
        }
    }

