buildsys.task.state.change
--------------------------
::

    {
        "$id": "/v1/buildsys.task.state.change#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A koji task state changed.",
        "type": "object",
        "properties": {
            "info": {
                "type": "object",
                "description": "task info",
                "properties": {
                    "parent": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "description": "parent tasks"
                    },
                    "completion_time": {
                        "type": "number",
                        "description": "completion time"
                    },
                    "start_time": {
                        "type": "number",
                        "description": "start time"
                    },
                    "request": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "description": "task request details",
                        "contains": {
                            "type": "string"
                        }
                    },
                    "waiting": {
                        "type": "boolean",
                        "description": "Is the task waiting or not"
                    },
                    "awaited": {
                        "type": "null",
                        "description": "awaited"
                    },
                    "id": {
                        "type": "integer",
                        "description": "id"
                    },
                    "priority": {
                        "type": "integer",
                        "description": "priority"
                    },
                    "channel_id": {
                        "type": "integer",
                        "description": "channel_id"
                    },
                    "state": {
                        "type": "integer",
                        "description": "task state"
                    },
                    "create_time": {
                        "type": "number",
                        "description": "create time"
                    },
                    "result": {
                        "type": "null",
                        "description": "result"
                    },
                    "owner": {
                        "type": [
                            "null",
                            "string",
                            "integer"
                        ],
                        "description": "owner name or id"
                    },
                    "host_id": {
                        "type": "integer",
                        "description": "host id"
                    },
                    "method": {
                        "type": "string",
                        "description": "task method"
                    },
                    "label": {
                        "type": "null",
                        "description": "label"
                    },
                    "arch": {
                        "type": "string",
                        "description": "task specific architecture"
                    },
                    "children": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "description": "task childrens"
                    }
                }
            },
            "old": {
                "type": "string",
                "description": "previous task state"
            },
            "attribute": {
                "type": "string",
                "description": "attribute"
            },
            "id": {
                "type": "integer",
                "description": "task id"
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji"
            },
            "owner": {
                "type": "string",
                "description": "name of the package owner"
            },
            "new": {
                "type": "string",
                "description": "name of the new task state"
            },
            "srpm": {
                "type": "string",
                "description": "name of the source rpm"
            },
            "method": {
                "type": "string",
                "description": "name of the task method"
            }
        }
    }

