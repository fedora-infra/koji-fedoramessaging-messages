buildsys.package.list.change
----------------------------
::

    {
        "$id": "/v1/buildsys.package.list.change#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package list changed.",
        "type": "object",
        "properties": {
            "force": {
                "type": [
                    "null",
                    "boolean"
                ],
                "description": "force"
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji"
            },
            "extra_arches": {
                "type": [
                    "null",
                    "string"
                ],
                "description": "extra arches"
            },
            "package": {
                "type": "string",
                "description": "name of the package updated"
            },
            "update": {
                "type": [
                    "null",
                    "boolean"
                ],
                "description": "update"
            },
            "owner": {
                "type": [
                    "null",
                    "string"
                ],
                "description": "name of the package owner"
            },
            "tag": {
                "type": "string",
                "description": "name of the tag"
            },
            "action": {
                "type": "string",
                "description": "name of the action"
            },
            "block": {
                "type": [
                    "null",
                    "boolean"
                ],
                "description": "block"
            }
        }
    }

