from koji_fedoramessaging_messages.build import BuildStateChangeV1


def test_build_state_change_message():
    body = {
        "build_id": 1478312,
        "old": 0,
        "name": "chromium",
        "task_id": None,
        "task": None,
        "attribute": "state",
        "request": [
            (
                "git+https://src.fedoraproject.org/rpms/chromium.git#"
                "5f8f367e482fe8e30711aea49bf2ecfd163d278f"
            ),
            "rawhide",
            {},
        ],
        "instance": "primary",
        "epoch": None,
        "version": "80.0.3987.132",
        "owner": "spot",
        "new": 1,
        "release": "1.fc33",
        "creation_time": "2023-06-09T07:16:27.818161+00:00",
        "completion_time": "2023-06-09T07:35:14.682273+00:00",
        "url": "https://koji.fedoraproject.org/koji/buildinfo?taskID=1478312",
    }

    msg = BuildStateChangeV1(body=body)
    msg.validate()
    assert msg.build_id == 1478312
    assert msg.name == "chromium"
    assert msg.owner == "spot"
    assert msg.version == "80.0.3987.132"
    assert msg.release == "1.fc33"
    assert msg.old == 0
    assert msg.old_state_name == "building"
    assert msg.new == 1
    assert msg.task_id is None
    assert msg.attribute == "state"
    assert msg.request == body["request"]
    assert msg.instance == "primary"
    assert msg.epoch is None
    assert msg.url == "https://koji.fedoraproject.org/koji/buildinfo?taskID=1478312"

    assert msg.agent_name == "spot"
    assert msg.summary == "Build COMPLETE: spot's chromium-80.0.3987.132-1.fc33"
    assert msg.packages == ["chromium"]
    expected_str = """Package:    chromium-80.0.3987.132-1.fc33
Status:     complete
Built by:   spot
ID:         1478312
Started:    Fri, 09 Jun 2023 07:16:27 UTC
Finished:   Fri, 09 Jun 2023 07:35:14 UTC

Build imported into koji
"""
    assert str(msg) == expected_str


def test_build_state_change_message_with_task():
    body = {
        "build_id": 1478312,
        "old": 0,
        "name": "chromium",
        "task_id": 42561864,
        "attribute": "state",
        "request": [
            (
                "git+https://src.fedoraproject.org/rpms/chromium.git#"
                "5f8f367e482fe8e30711aea49bf2ecfd163d278f"
            ),
            "rawhide",
            {},
        ],
        "instance": "primary",
        "epoch": None,
        "version": "80.0.3987.132",
        "owner": "spot",
        "new": 1,
        "release": "1.fc33",
        "creation_time": "2023-06-09T07:16:27.818161+00:00",
        "completion_time": "2023-06-09T07:35:14.682273+00:00",
        "files_base_url": "http://files.example.com/work",
        "task": {
            "parent": None,
            "completion_time": 1584475720.0,
            "start_time": 1584475492.0,
            "request": [
                (
                    "git+https://src.fedoraproject.org/rpms/chromium.git#"
                    "5f8f367e482fe8e30711aea49bf2ecfd163d278f"
                ),
                "rawhide",
                {},
            ],
            "waiting": False,
            "awaited": None,
            "id": 42561864,
            "priority": 20,
            "channel_id": 19,
            "state": 2,
            "create_time": 1584475491.0,
            "owner": 3199,
            "host_id": 306,
            "host_name": "buildvm-armv7-19.arm.fedoraproject.org",
            "method": "build",
            "label": None,
            "arch": "noarch",
            "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=42561864",
            "result": None,
            "children": [],
        },
    }

    msg = BuildStateChangeV1(body=body)
    msg.validate()
    assert msg.build_id == 1478312
    assert msg.name == "chromium"
    assert msg.owner == "spot"
    assert msg.version == "80.0.3987.132"
    assert msg.release == "1.fc33"
    assert msg.old == 0
    assert msg.new == 1
    assert msg.task_id == 42561864
    assert msg.attribute == "state"
    assert msg.request == body["request"]
    assert msg.instance == "primary"
    assert msg.epoch is None

    assert msg.agent_name == "spot"
    assert msg.summary == "Build COMPLETE: spot's chromium-80.0.3987.132-1.fc33"
    assert msg.packages == ["chromium"]
    expected_str = """Package:    chromium-80.0.3987.132-1.fc33
Status:     complete
Built by:   spot
ID:         1478312
Started:    Fri, 09 Jun 2023 07:16:27 UTC
Finished:   Fri, 09 Jun 2023 07:35:14 UTC

Closed tasks:
-------------
Task 42561864 on buildvm-armv7-19.arm.fedoraproject.org
Task Type: build (noarch)
Link: https://koji.fedoraproject.org/koji/taskinfo?taskID=42561864
"""
    assert str(msg) == expected_str


def test_build_not_finished():
    body = {
        "build_id": 1478312,
        "old": None,
        "name": "chromium",
        "task_id": None,
        "task": None,
        "attribute": "state",
        "request": [
            (
                "git+https://src.fedoraproject.org/rpms/chromium.git#"
                "5f8f367e482fe8e30711aea49bf2ecfd163d278f"
            ),
            "rawhide",
            {},
        ],
        "instance": "primary",
        "epoch": None,
        "version": "80.0.3987.132",
        "owner": "spot",
        "new": 0,
        "release": "1.fc33",
        "creation_time": "2023-06-09T07:16:27.818161+00:00",
        "completion_time": None,
        "url": "https://koji.fedoraproject.org/koji/buildinfo?taskID=1478312",
    }

    msg = BuildStateChangeV1(body=body)
    msg.validate()
    expected_str = """Package:    chromium-80.0.3987.132-1.fc33
Status:     building
Built by:   spot
ID:         1478312
Started:    Fri, 09 Jun 2023 07:16:27 UTC
Finished:   (still running)

Build imported into koji
"""
    assert str(msg) == expected_str
