from koji_fedoramessaging_messages.build import BuildStateChangeV1


def test_build_state_change_message():

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
