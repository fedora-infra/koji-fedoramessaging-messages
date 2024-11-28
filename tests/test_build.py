# SPDX-FileCopyrightText: 2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pytest
from jsonschema.exceptions import ValidationError

from koji_fedoramessaging_messages.build import BUILD_STATES, BuildStateChangeV1


@pytest.fixture
def msg_build_complete():
    return {
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


def test_build_state_change_message(msg_build_complete):
    msg = BuildStateChangeV1(body=msg_build_complete)
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
    assert msg.request == msg_build_complete["request"]
    assert msg.instance == "primary"
    assert msg.epoch is None
    assert msg.url == "https://koji.fedoraproject.org/koji/buildinfo?taskID=1478312"

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


def test_build_state_change_message_with_task(msg_build_complete):
    msg_build_complete.update(
        {
            "files_base_url": "http://files.example.com/work",
            "task_id": 42561864,
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
    )

    msg = BuildStateChangeV1(body=msg_build_complete)
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
    assert msg.request == msg_build_complete["request"]
    assert msg.instance == "primary"
    assert msg.epoch is None

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


def test_build_not_finished(msg_build_complete):
    msg_build_complete.update(
        {
            "old": None,
            "new": 0,
            "completion_time": None,
        }
    )
    msg = BuildStateChangeV1(body=msg_build_complete)
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


def test_build_state_change_message_with_task_no_start_time(msg_build_complete):
    msg_build_complete.update(
        {
            "task": {
                "start_time": None,
                # The rest is normal
                "id": 42561864,
                "host_id": None,
                "method": "build",
                "arch": "noarch",
                "result": None,
            },
        }
    )
    msg = BuildStateChangeV1(body=msg_build_complete)
    try:
        msg.validate()
    except ValidationError:
        pytest.fail("The message didn't validate with start_time == None")


def test_build_no_request(msg_build_complete):
    msg_build_complete["request"] = None
    msg = BuildStateChangeV1(body=msg_build_complete)
    try:
        msg.validate()
    except ValidationError:
        pytest.fail("The message didn't validate with request == None")
    assert msg.request is None


@pytest.mark.parametrize(
    ["oldstate", "newstate", "agent_name"],
    [
        (None, BUILD_STATES.BUILDING.value, "spot"),
        (BUILD_STATES.BUILDING.value, BUILD_STATES.COMPLETE.value, None),
        (BUILD_STATES.BUILDING.value, BUILD_STATES.FAILED.value, None),
        (BUILD_STATES.BUILDING.value, BUILD_STATES.CANCELED.value, "spot"),
        (BUILD_STATES.COMPLETE.value, BUILD_STATES.DELETED.value, None),
        (BUILD_STATES.FAILED.value, BUILD_STATES.DELETED.value, None),
    ],
)
def test_build_users(msg_build_complete, oldstate, newstate, agent_name):
    msg_build_complete.update(
        {
            "old": oldstate,
            "new": newstate,
        }
    )
    msg = BuildStateChangeV1(body=msg_build_complete)
    msg.validate()
    assert msg.agent_name == agent_name
    assert msg.usernames == ["spot"]


def test_build_state_change_livecd():
    # LiveCD results are a string, not a list of artifacts
    body = {
        "base_url": "https://koji.fedoraproject.org",
        "name": "Fedora-i3-Live",
        "version": "Rawhide",
        "release": "20240101.n.0",
        "epoch": 0,
        "attribute": "state",
        "old": 1,
        "new": 2,
        "build_id": 2339329,
        "task_id": 111136700,
        "owner": "releng",
        "files_base_url": "https://kojipkgs.fedoraproject.org/work",
        "url": "https://koji.fedoraproject.org/koji/buildinfo?buildID=2339329",
        "task": {
            "arch": "noarch",
            "awaited": None,
            "channel_id": 13,
            "completion_time": 1704095980.0,
            "create_time": 1704094624.0,
            "host_id": 502,
            "id": 111136700,
            "label": None,
            "method": "livemedia",
            "owner": "releng",
            "parent": None,
            "priority": 20,
            "start_time": 1704094664.0,
            "state": 2,
            "waiting": False,
            "request": [
                "Fedora-i3-Live",
                "Rawhide",
                ["aarch64", "x86_64"],
                "f40",
                "fedora-live-i3.ks",
                {
                    "install_tree_url": (
                        "https://kojipkgs.fedoraproject.org/compose/rawhide/Fedora-Rawhide-20240101.n.0/compose/Everything/$basearch/os"
                    ),
                    "ksurl": "git+https://pagure.io/fedora-kickstarts.git?#eab4fdc148f58e61d17e975c2dfe6181137daaa4",
                    "release": "20240101.n.0",
                    "repo": [
                        "https://kojipkgs.fedoraproject.org/compose/rawhide/Fedora-Rawhide-20240101.n.0/compose/Everything/$basearch/os"
                    ],
                    "optional_arches": ["aarch64", "x86_64"],
                    "compress_arg": [],
                },
            ],
            "host_name": "buildhw-x86-13.iad2.fedoraproject.org",
            "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=111136700",
            "result": (
                "livecd build results in: "
                "/mnt/koji/packages/Fedora-i3-Live/Rawhide/20240101.n.0/images"
            ),
            "children": [
                {
                    "arch": "noarch",
                    "awaited": False,
                    "channel_id": 13,
                    "completion_time": 1704095979.0,
                    "create_time": 1704095967.0,
                    "host_id": 503,
                    "id": 111137305,
                    "label": "tag",
                    "method": "tagBuild",
                    "owner": "releng",
                    "parent": 111136700,
                    "priority": 19,
                    "start_time": 1704095979.0,
                    "state": 2,
                    "waiting": None,
                    "host_name": "buildhw-x86-14.iad2.fedoraproject.org",
                    "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=111137305",
                    "result": None,
                    "children": [],
                },
                {
                    "arch": "x86_64",
                    "awaited": False,
                    "channel_id": 13,
                    "completion_time": 1704095927.0,
                    "create_time": 1704094664.0,
                    "host_id": 392,
                    "id": 111136748,
                    "label": "livemedia x86_64",
                    "method": "createLiveMedia",
                    "owner": "releng",
                    "parent": 111136700,
                    "priority": 19,
                    "start_time": 1704094735.0,
                    "state": 2,
                    "waiting": None,
                    "host_name": "buildvm-x86-21.iad2.fedoraproject.org",
                    "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=111136748",
                    "result": {
                        "arch": "x86_64",
                        "files": ["Fedora-i3-Live-x86_64-Rawhide-20240101.n.0.iso"],
                        "rootdev": None,
                        "task_id": 111136748,
                        "logs": [
                            "build.log",
                            "mock_output.log",
                            "root.log",
                            "state.log",
                            "livemedia-out.log",
                            "fedora-live-i3.ks",
                            "koji-image-f40-build-111136748.ks",
                        ],
                        "name": "Fedora-i3-Live",
                        "version": "Rawhide",
                        "release": "20240101.n.0",
                        "rpmlist": [],
                    },
                    "children": [],
                },
                {
                    "arch": "aarch64",
                    "awaited": False,
                    "channel_id": 13,
                    "completion_time": 1704095791.0,
                    "create_time": 1704094664.0,
                    "host_id": 542,
                    "id": 111136747,
                    "label": "livemedia aarch64",
                    "method": "createLiveMedia",
                    "owner": "releng",
                    "parent": 111136700,
                    "priority": 19,
                    "start_time": 1704094704.0,
                    "state": 2,
                    "waiting": None,
                    "host_name": "buildhw-a64-21.iad2.fedoraproject.org",
                    "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=111136747",
                    "result": {
                        "arch": "aarch64",
                        "files": ["Fedora-i3-Live-aarch64-Rawhide-20240101.n.0.iso"],
                        "rootdev": None,
                        "task_id": 111136747,
                        "logs": [
                            "build.log",
                            "mock_output.log",
                            "root.log",
                            "state.log",
                            "livemedia-out.log",
                            "fedora-live-i3.ks",
                            "koji-image-f40-build-111136747.ks",
                        ],
                        "name": "Fedora-i3-Live",
                        "version": "Rawhide",
                        "release": "20240101.n.0",
                        "rpmlist": [],
                    },
                    "children": [],
                },
            ],
        },
        "request": [
            "Fedora-i3-Live",
            "Rawhide",
            ["aarch64", "x86_64"],
            "f40",
            "fedora-live-i3.ks",
            {
                "install_tree_url": "https://kojipkgs.fedoraproject.org/compose/rawhide/Fedora-Rawhide-20240101.n.0/compose/Everything/$basearch/os",
                "ksurl": "git+https://pagure.io/fedora-kickstarts.git?#eab4fdc148f58e61d17e975c2dfe6181137daaa4",
                "release": "20240101.n.0",
                "repo": [
                    "https://kojipkgs.fedoraproject.org/compose/rawhide/Fedora-Rawhide-20240101.n.0/compose/Everything/$basearch/os"
                ],
                "optional_arches": ["aarch64", "x86_64"],
                "compress_arg": [],
            },
        ],
        "creation_time": "2024-01-01T07:37:44.691478+00:00",
        "completion_time": "2024-01-01T07:59:10.566171+00:00",
        "instance": "primary",
    }
    msg = BuildStateChangeV1(body=body)
    msg.validate()
