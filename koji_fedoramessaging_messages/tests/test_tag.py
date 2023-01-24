from koji_fedoramessaging_messages.tag import TagV1, UntagV1


def test_tag_message():

    body = {
        "build_id": 1457909,
        "name": "http-parser",
        "tag_id": 6446,
        "instance": "primary",
        "tag": "f31-updates-pending",
        "user": "bodhi",
        "version": "2.9.3",
        "owner": "sgallagh",
        "release": "1.fc31",
    }

    msg = TagV1(body=body)
    msg.validate()
    assert msg.build_id == 1457909
    assert msg.name == "http-parser"
    assert msg.tag == "f31-updates-pending"
    assert msg.tag_id == 6446
    assert msg.instance == "primary"
    assert msg.user == "bodhi"
    assert msg.owner == "sgallagh"
    assert msg.version == "2.9.3"
    assert msg.release == "1.fc31"


def test_untag_message():

    body = {
        "build_id": 1478431,
        "name": "python-twisted",
        "tag_id": 10321,
        "instance": "primary",
        "tag": "epel8-signing-pending",
        "user": "autopen",
        "version": "19.10.0",
        "owner": "eclipseo",
        "release": "2.el8",
    }

    msg = UntagV1(body=body)
    msg.validate()
    assert msg.build_id == 1478431
    assert msg.name == "python-twisted"
    assert msg.tag == "epel8-signing-pending"
    assert msg.tag_id == 10321
    assert msg.instance == "primary"
    assert msg.user == "autopen"
    assert msg.owner == "eclipseo"
    assert msg.version == "19.10.0"
    assert msg.release == "2.el8"
