buildsys.tag
------------
::

    {
        "$id": "/v1/buildsys.tag#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package is tagged.",
        "type": "object",
        "properties": {
            "build_id": {
                "type": "integer",
                "description": "build id"
            },
            "name": {
                "type": "string",
                "description": "package name"
            },
            "tag_id": {
                "type": "integer",
                "description": "tag id"
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji"
            },
            "tag": {
                "type": "string",
                "description": "name of the tag"
            },
            "user": {
                "type": "string",
                "description": "name of the user that trigger the build"
            },
            "version": {
                "type": "string",
                "description": "version of the build"
            },
            "owner": {
                "type": "string",
                "description": "name of the package owner"
            },
            "release": {
                "type": "string",
                "description": "release number of the package"
            }
        }
    }

buildsys.untag
--------------
::

    {
        "$id": "/v1/buildsys.untag#",
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "description": "A package is untagged.",
        "type": "object",
        "properties": {
            "build_id": {
                "type": "integer",
                "description": "build id"
            },
            "name": {
                "type": "string",
                "description": "package name"
            },
            "tag_id": {
                "type": "integer",
                "description": "tag id"
            },
            "instance": {
                "type": "string",
                "description": "distinguish between messages from primary and secondary koji"
            },
            "tag": {
                "type": "string",
                "description": "name of the tag"
            },
            "user": {
                "type": "string",
                "description": "name of the user that trigger the build"
            },
            "version": {
                "type": "string",
                "description": "version of the build"
            },
            "owner": {
                "type": "string",
                "description": "name of the package owner"
            },
            "release": {
                "type": "string",
                "description": "release number of the package"
            }
        }
    }

