# koji-fedmsg-plugin

Koji plugin to send messages on fedora-messaging


# Development environment

```
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install poetry
(.venv) $ poetry install
```

# Running the tests

```
$ poetry run pytest
```

# Building the docs

Generate the json schema

```
$ cd docs
$ python generate_json_schema.py
```

Build the html

```
$ cd docs
$ make html
```
