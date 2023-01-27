from koji_fedoramessaging_messages.task import TaskStateChangeV1


def test_task_state_change_message():

    body = {
        "info": {
            "parent": None,
            "completion_time": 1584475720.0,
            "start_time": 1584475492.0,
            "request": [
                "../packages/libfreehand/0.1.2/6.fc32/src/libfreehand-0.1.2-6.fc32.src.rpm",
                "f33",
                {"scratch": True, "arch_override": "ppc64le x86_64 aarch64"},
            ],
            "waiting": False,
            "awaited": None,
            "id": 42569071,
            "priority": 50,
            "channel_id": 1,
            "state": 2,
            "create_time": 1584475491.0,
            "result": None,
            "owner": 3199,
            "host_id": 303,
            "method": "build",
            "label": None,
            "arch": "noarch",
            "children": [
                {
                    "parent": 42569071,
                    "completion_time": 1584475672.0,
                    "start_time": 1584475573.0,
                    "waiting": None,
                    "awaited": False,
                    "label": "ppc64le",
                    "priority": 49,
                    "channel_id": 1,
                    "state": 2,
                    "create_time": 1584475570.0,
                    "owner": 3199,
                    "host_id": 358,
                    "method": "buildArch",
                    "arch": "ppc64le",
                    "id": 42569109,
                },
                {
                    "parent": 42569071,
                    "completion_time": 1584475719.0,
                    "start_time": 1584475591.0,
                    "waiting": None,
                    "awaited": False,
                    "label": "aarch64",
                    "priority": 49,
                    "channel_id": 1,
                    "state": 2,
                    "create_time": 1584475570.0,
                    "owner": 3199,
                    "host_id": 222,
                    "method": "buildArch",
                    "arch": "aarch64",
                    "id": 42569111,
                },
                {
                    "parent": 42569071,
                    "completion_time": 1584475658.0,
                    "start_time": 1584475571.0,
                    "waiting": None,
                    "awaited": False,
                    "label": "x86_64",
                    "priority": 49,
                    "channel_id": 1,
                    "state": 2,
                    "create_time": 1584475570.0,
                    "owner": 3199,
                    "host_id": 71,
                    "method": "buildArch",
                    "arch": "x86_64",
                    "id": 42569110,
                },
                {
                    "parent": 42569071,
                    "completion_time": 1584475554.0,
                    "start_time": 1584475493.0,
                    "waiting": None,
                    "awaited": False,
                    "label": "srpm",
                    "priority": 49,
                    "channel_id": 1,
                    "state": 2,
                    "create_time": 1584475492.0,
                    "owner": 3199,
                    "host_id": 204,
                    "method": "rebuildSRPM",
                    "arch": "noarch",
                    "id": 42569074,
                },
            ],
        },
        "old": "OPEN",
        "attribute": "state",
        "id": 42569071,
        "instance": "primary",
        "owner": "koschei",
        "new": "CLOSED",
        "srpm": "libfreehand-0.1.2-6.fc32.src.rpm",
        "method": "build",
    }

    msg = TaskStateChangeV1(body=body)
    msg.validate()
    assert msg.old == "OPEN"
    assert msg.new == "CLOSED"
    assert msg.method == "build"
    assert msg.info["create_time"] == 1584475491.0
    assert msg.info["children"][0]["arch"] == "ppc64le"
    assert msg.attribute == "state"
    assert msg.id == 42569071
    assert msg.instance == "primary"
    assert msg.owner == "koschei"
    assert msg.srpm == "libfreehand-0.1.2-6.fc32.src.rpm"
    assert (
        msg.summary == "Task CLOSED -- build (libfreehand-0.1.2-6.fc32.src.rpm noarch)"
    )
