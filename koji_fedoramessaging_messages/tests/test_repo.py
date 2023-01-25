from koji_fedoramessaging_messages.repo import DoneV1, InitV1


def test_repo_done_message():

    body = {
        "instance": "primary",
        "repo_id": 1409150,
        "tag": "module-jmc-latest-3220200311144307-089fddd9-build",
        "tag_id": 20164,
    }

    msg = DoneV1(body=body)
    msg.validate()
    assert msg.instance == "primary"
    assert msg.tag == "module-jmc-latest-3220200311144307-089fddd9-build"
    assert msg.tag_id == 20164
    assert msg.repo_id == 1409150

    assert msg.owner is None
    assert msg.agent_name is None
    assert msg.agent_avatar is None


def test_repo_init_message():

    body = {
        "instance": "primary",
        "repo_id": 1410901,
        "tag": "f33-build",
        "tag_id": 18677,
    }

    msg = InitV1(body=body)
    msg.validate()
    assert msg.instance == "primary"
    assert msg.tag == "f33-build"
    assert msg.tag_id == 18677
    assert msg.repo_id == 1410901

    assert msg.owner is None
    assert msg.agent_name is None
    assert msg.agent_avatar is None
