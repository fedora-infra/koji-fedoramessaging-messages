from koji_fedoramessaging_messages.package import ListChangeV1


def test_package_list_change_message1():

    body = {
        "force": None,
        "instance": "primary",
        "extra_arches": None,
        "package": "rust-ripgrep",
        "update": None,
        "owner": None,
        "tag": "f31",
        "action": "unblock",
        "block": None,
    }

    msg = ListChangeV1(body=body)
    msg.validate()
    assert msg.force is None
    assert msg.package == "rust-ripgrep"
    assert msg.owner is None
    assert msg.update is None
    assert msg.action == "unblock"
    assert msg.tag == "f31"
    assert msg.block is None
    assert msg.instance == "primary"
    assert msg.extra_arches is None


def test_package_list_change_message2():

    body = {
        "force": True,
        "instance": "primary",
        "extra_arches": "",
        "package": "rust-dua-cli",
        "update": False,
        "owner": "releng",
        "tag": "f31-build-side-20267",
        "action": "add",
        "block": False,
    }

    msg = ListChangeV1(body=body)
    msg.validate()
    assert msg.force
    assert msg.package == "rust-dua-cli"
    assert msg.owner == "releng"
    assert not msg.update
    assert msg.action == "add"
    assert msg.tag == "f31-build-side-20267"
    assert not msg.block
    assert msg.instance == "primary"
    assert msg.extra_arches == ""

    assert msg.agent_name == "releng"
    assert msg.summary == "Package list change for rust-dua-cli:  f31-build-side-20267"
