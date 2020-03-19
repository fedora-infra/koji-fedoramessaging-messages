buildsys.repo.done
------------------
::

    {
        "$id": "/v1/buildsys.repo.done#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package repo task was done.",
        "type": "object",
        "properties": {
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji"
            },
            "repo_id": {
                "type": "integer",
                "description": "repo id"
            },
            "tag": {
                "type": "string",
                "description": "tag used to generate the repo"
            },
            "tag_id": {
                "type": "integer",
                "description": "tag id of the tag used to generate the repo"
            }
        }
    }

buildsys.repo.init
------------------
::

    {
        "$id": "/v1/buildsys.repo.init#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package repo task is initialized.",
        "type": "object",
        "properties": {
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji."
            },
            "repo_id": {
                "type": "integer",
                "description": "repo id"
            },
            "tag": {
                "type": "string",
                "description": "tag used to generate the repo"
            },
            "tag_id": {
                "type": "integer",
                "description": "tag id of the tag used to generate the repo"
            }
        }
    }

