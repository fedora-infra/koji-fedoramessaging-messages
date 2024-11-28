# SPDX-FileCopyrightText: 2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

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
            "owner": 3199,
            "host_id": 303,
            "host_name": "buildvm-armv7-16.arm.fedoraproject.org",
            "method": "build",
            "label": None,
            "arch": "noarch",
            "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569071",
            "result": None,
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
                    "host_name": "buildvm-ppc64le-27.ppc.fedoraproject.org",
                    "method": "buildArch",
                    "arch": "ppc64le",
                    "id": 42569109,
                    "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569109",
                    "children": [],
                    "result": {
                        "rpms": [
                            "tasks/9109/42569109/libfreehand-tools-debuginfo-0.1.2-6.fc33.ppc64le.rpm",
                            "tasks/9109/42569109/libfreehand-doc-0.1.2-6.fc33.noarch.rpm",
                            "tasks/9109/42569109/libfreehand-tools-0.1.2-6.fc33.ppc64le.rpm",
                            "tasks/9109/42569109/libfreehand-debugsource-0.1.2-6.fc33.ppc64le.rpm",
                            "tasks/9109/42569109/libfreehand-0.1.2-6.fc33.ppc64le.rpm",
                            "tasks/9109/42569109/libfreehand-debuginfo-0.1.2-6.fc33.ppc64le.rpm",
                            "tasks/9109/42569109/libfreehand-devel-0.1.2-6.fc33.ppc64le.rpm",
                        ],
                        "srpms": ["tasks/9109/42569109/libfreehand-0.1.2-6.fc33.src.rpm"],
                        "logs": [
                            "tasks/9109/42569109/root.log",
                            "tasks/9109/42569109/hw_info.log",
                            "tasks/9109/42569109/state.log",
                            "tasks/9109/42569109/build.log",
                            "tasks/9109/42569109/mock_output.log",
                            "tasks/9109/42569109/noarch_rpmdiff.json",
                        ],
                        "brootid": 19891114,
                    },
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
                    "host_name": "buildvm-aarch64-25.arm.fedoraproject.org",
                    "method": "buildArch",
                    "arch": "aarch64",
                    "id": 42569111,
                    "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569111",
                    "children": [],
                    "result": {
                        "rpms": [
                            "tasks/9111/42569111/libfreehand-tools-debuginfo-0.1.2-6.fc33.aarch64.rpm",
                            "tasks/9111/42569111/libfreehand-devel-0.1.2-6.fc33.aarch64.rpm",
                            "tasks/9111/42569111/libfreehand-doc-0.1.2-6.fc33.noarch.rpm",
                            "tasks/9111/42569111/libfreehand-tools-0.1.2-6.fc33.aarch64.rpm",
                            "tasks/9111/42569111/libfreehand-0.1.2-6.fc33.aarch64.rpm",
                            "tasks/9111/42569111/libfreehand-debuginfo-0.1.2-6.fc33.aarch64.rpm",
                            "tasks/9111/42569111/libfreehand-debugsource-0.1.2-6.fc33.aarch64.rpm",
                        ],
                        "srpms": [],
                        "logs": [
                            "tasks/9111/42569111/build.log",
                            "tasks/9111/42569111/root.log",
                            "tasks/9111/42569111/hw_info.log",
                            "tasks/9111/42569111/state.log",
                            "tasks/9111/42569111/mock_output.log",
                            "tasks/9111/42569111/noarch_rpmdiff.json",
                        ],
                        "brootid": 19891120,
                    },
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
                    "host_name": "buildvm-13.phx2.fedoraproject.org",
                    "method": "buildArch",
                    "arch": "x86_64",
                    "id": 42569110,
                    "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569110",
                    "children": [],
                    "result": {
                        "rpms": [
                            "tasks/9110/42569110/libfreehand-0.1.2-6.fc33.x86_64.rpm",
                            "tasks/9110/42569110/libfreehand-debugsource-0.1.2-6.fc33.x86_64.rpm",
                            "tasks/9110/42569110/libfreehand-devel-0.1.2-6.fc33.x86_64.rpm",
                            "tasks/9110/42569110/libfreehand-debuginfo-0.1.2-6.fc33.x86_64.rpm",
                            "tasks/9110/42569110/libfreehand-tools-0.1.2-6.fc33.x86_64.rpm",
                            "tasks/9110/42569110/libfreehand-doc-0.1.2-6.fc33.noarch.rpm",
                            "tasks/9110/42569110/libfreehand-tools-debuginfo-0.1.2-6.fc33.x86_64.rpm",
                        ],
                        "srpms": [],
                        "logs": [
                            "tasks/9110/42569110/hw_info.log",
                            "tasks/9110/42569110/state.log",
                            "tasks/9110/42569110/build.log",
                            "tasks/9110/42569110/root.log",
                            "tasks/9110/42569110/mock_output.log",
                            "tasks/9110/42569110/noarch_rpmdiff.json",
                        ],
                        "brootid": 19891112,
                    },
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
                    "host_name": "buildvm-aarch64-07.arm.fedoraproject.org",
                    "method": "rebuildSRPM",
                    "arch": "noarch",
                    "id": 42569074,
                    "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569074",
                    "children": [],
                    "result": {
                        "srpm": "tasks/9074/42569074/libfreehand-0.1.2-6.fc33.src.rpm",
                        "logs": [
                            "tasks/1391/110011391/hw_info.log",
                            "tasks/1391/110011391/state.log",
                            "tasks/1391/110011391/build.log",
                            "tasks/1391/110011391/root.log",
                            "tasks/1391/110011391/mock_output.log",
                            "tasks/1391/110011391/noarch_rpmdiff.json",
                        ],
                        "brootid": 19891084,
                        "source": {
                            "source": "libfreehand-0.1.2-6.fc33.src.rpm",
                            "url": "libfreehand-0.1.2-6.fc33.src.rpm",
                        },
                    },
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
        "base_url": "https://koji.stg.fedoraproject.org",
        "files_base_url": "http://files.example.com/work",
    }

    msg = TaskStateChangeV1(body=body)
    msg.validate()
    assert msg.old == "OPEN"
    assert msg.new == "CLOSED"
    assert msg.method == "build"
    assert msg.info["create_time"] == 1584475491.0
    assert msg.info["children"][0]["arch"] == "ppc64le"
    assert msg.attribute == "state"
    assert msg.task_id == 42569071
    assert msg.instance == "primary"
    assert msg.owner == "koschei"
    assert msg.srpm == "libfreehand-0.1.2-6.fc32.src.rpm"
    assert msg.url == "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569071"
    assert msg.summary == "Task CLOSED -- build (libfreehand-0.1.2-6.fc32.src.rpm noarch)"
    expected_str = """Task 42569071 on buildvm-armv7-16.arm.fedoraproject.org
Task Type: build (noarch)
Link: https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569071

Task 42569071 has the following sub-tasks:

Task 42569074 on buildvm-aarch64-07.arm.fedoraproject.org
Task Type: rebuildSRPM (noarch)
Link: https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569074
logs:
  http://files.example.com/work/tasks/1391/110011391/hw_info.log
  http://files.example.com/work/tasks/1391/110011391/state.log
  http://files.example.com/work/tasks/1391/110011391/build.log
  http://files.example.com/work/tasks/1391/110011391/root.log
  http://files.example.com/work/tasks/1391/110011391/mock_output.log
  http://files.example.com/work/tasks/1391/110011391/noarch_rpmdiff.json
srpm:
  http://files.example.com/work/tasks/9074/42569074/libfreehand-0.1.2-6.fc33.src.rpm

Task 42569110 on buildvm-13.phx2.fedoraproject.org
Task Type: buildArch (x86_64)
Link: https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569110
logs:
  http://files.example.com/work/tasks/9110/42569110/hw_info.log
  http://files.example.com/work/tasks/9110/42569110/state.log
  http://files.example.com/work/tasks/9110/42569110/build.log
  http://files.example.com/work/tasks/9110/42569110/root.log
  http://files.example.com/work/tasks/9110/42569110/mock_output.log
  http://files.example.com/work/tasks/9110/42569110/noarch_rpmdiff.json
rpms:
  http://files.example.com/work/tasks/9110/42569110/libfreehand-0.1.2-6.fc33.x86_64.rpm
  http://files.example.com/work/tasks/9110/42569110/libfreehand-debugsource-0.1.2-6.fc33.x86_64.rpm
  http://files.example.com/work/tasks/9110/42569110/libfreehand-devel-0.1.2-6.fc33.x86_64.rpm
  http://files.example.com/work/tasks/9110/42569110/libfreehand-debuginfo-0.1.2-6.fc33.x86_64.rpm
  http://files.example.com/work/tasks/9110/42569110/libfreehand-tools-0.1.2-6.fc33.x86_64.rpm
  http://files.example.com/work/tasks/9110/42569110/libfreehand-doc-0.1.2-6.fc33.noarch.rpm
  http://files.example.com/work/tasks/9110/42569110/libfreehand-tools-debuginfo-0.1.2-6.fc33.x86_64.rpm

Task 42569109 on buildvm-ppc64le-27.ppc.fedoraproject.org
Task Type: buildArch (ppc64le)
Link: https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569109
logs:
  http://files.example.com/work/tasks/9109/42569109/root.log
  http://files.example.com/work/tasks/9109/42569109/hw_info.log
  http://files.example.com/work/tasks/9109/42569109/state.log
  http://files.example.com/work/tasks/9109/42569109/build.log
  http://files.example.com/work/tasks/9109/42569109/mock_output.log
  http://files.example.com/work/tasks/9109/42569109/noarch_rpmdiff.json
rpms:
  http://files.example.com/work/tasks/9109/42569109/libfreehand-tools-debuginfo-0.1.2-6.fc33.ppc64le.rpm
  http://files.example.com/work/tasks/9109/42569109/libfreehand-doc-0.1.2-6.fc33.noarch.rpm
  http://files.example.com/work/tasks/9109/42569109/libfreehand-tools-0.1.2-6.fc33.ppc64le.rpm
  http://files.example.com/work/tasks/9109/42569109/libfreehand-debugsource-0.1.2-6.fc33.ppc64le.rpm
  http://files.example.com/work/tasks/9109/42569109/libfreehand-0.1.2-6.fc33.ppc64le.rpm
  http://files.example.com/work/tasks/9109/42569109/libfreehand-debuginfo-0.1.2-6.fc33.ppc64le.rpm
  http://files.example.com/work/tasks/9109/42569109/libfreehand-devel-0.1.2-6.fc33.ppc64le.rpm
srpms:
  http://files.example.com/work/tasks/9109/42569109/libfreehand-0.1.2-6.fc33.src.rpm

Task 42569111 on buildvm-aarch64-25.arm.fedoraproject.org
Task Type: buildArch (aarch64)
Link: https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=42569111
logs:
  http://files.example.com/work/tasks/9111/42569111/build.log
  http://files.example.com/work/tasks/9111/42569111/root.log
  http://files.example.com/work/tasks/9111/42569111/hw_info.log
  http://files.example.com/work/tasks/9111/42569111/state.log
  http://files.example.com/work/tasks/9111/42569111/mock_output.log
  http://files.example.com/work/tasks/9111/42569111/noarch_rpmdiff.json
rpms:
  http://files.example.com/work/tasks/9111/42569111/libfreehand-tools-debuginfo-0.1.2-6.fc33.aarch64.rpm
  http://files.example.com/work/tasks/9111/42569111/libfreehand-devel-0.1.2-6.fc33.aarch64.rpm
  http://files.example.com/work/tasks/9111/42569111/libfreehand-doc-0.1.2-6.fc33.noarch.rpm
  http://files.example.com/work/tasks/9111/42569111/libfreehand-tools-0.1.2-6.fc33.aarch64.rpm
  http://files.example.com/work/tasks/9111/42569111/libfreehand-0.1.2-6.fc33.aarch64.rpm
  http://files.example.com/work/tasks/9111/42569111/libfreehand-debuginfo-0.1.2-6.fc33.aarch64.rpm
  http://files.example.com/work/tasks/9111/42569111/libfreehand-debugsource-0.1.2-6.fc33.aarch64.rpm
"""
    assert str(msg) == expected_str
