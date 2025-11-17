# SPDX-FileCopyrightText: 2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json

import pytest
from fedora_messaging import message

from koji_fedoramessaging_messages.utilities import date_to_string


@pytest.mark.parametrize(
    "timestamp,expected",
    [("2023-06-09T07:16:27.818161+00:00", "Fri, 09 Jun 2023 07:16:27 UTC"), (None, "")],
)
def test_date_to_string(timestamp, expected):
    assert date_to_string(timestamp) == expected


def test_no_completion_time():
    # https://apps.fedoraproject.org/datagrepper/v2/id?id=eb9af16c-7324-4140-bc99-1822915f359b&is_raw=true&size=extra-large
    msg_dump = json.loads(
        """
{
  "body": {
    "attribute": "state",
    "base_url": "https://koji.fedoraproject.org",
    "build_id": 2860061,
    "completion_time": "2025-11-17T14:42:01.741593+00:00",
    "creation_time": "2025-11-17T13:10:36.335964+00:00",
    "epoch": null,
    "files_base_url": "https://kojipkgs.fedoraproject.org/work",
    "instance": "primary",
    "name": "prusa-slicer",
    "new": 4,
    "old": 0,
    "owner": "spot",
    "release": "1.fc44",
    "request": [
      "git+https://src.fedoraproject.org/rpms/prusa-slicer.git#ddbac739fc9482082b06028e5606f74c06e1db07",
      "rawhide",
      {}
    ],
    "task": {
      "arch": "noarch",
      "awaited": null,
      "channel_id": 1,
      "children": [
        {
          "arch": "s390x",
          "awaited": true,
          "channel_id": 1,
          "children": [],
          "completion_time": null,
          "create_time": 1763385036.0,
          "host_id": 324,
          "host_name": "buildvm-s390x-09.s390.fedoraproject.org",
          "id": 139004157,
          "label": "s390x",
          "method": "buildArch",
          "owner": "spot",
          "parent": 139004033,
          "priority": 19,
          "result": null,
          "start_time": 1763385104.0,
          "state": 1,
          "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=139004157",
          "waiting": null
        },
        {
          "arch": "ppc64le",
          "awaited": false,
          "channel_id": 1,
          "children": [],
          "completion_time": 1763388147.0,
          "create_time": 1763385036.0,
          "host_id": 665,
          "host_name": "buildvm-ppc64le-25.rdu3.fedoraproject.org",
          "id": 139004156,
          "label": "ppc64le",
          "method": "buildArch",
          "owner": "spot",
          "parent": 139004033,
          "priority": 19,
          "result": null,
          "start_time": 1763385096.0,
          "state": 5,
          "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=139004156",
          "waiting": null
        },
        {
          "arch": "x86_64",
          "awaited": false,
          "channel_id": 1,
          "children": [],
          "completion_time": 1763385034.0,
          "create_time": 1763384912.0,
          "host_id": 589,
          "host_name": "buildvm-x86-19.rdu3.fedoraproject.org",
          "id": 139004050,
          "label": "srpm",
          "method": "buildSRPMFromSCM",
          "owner": "spot",
          "parent": 139004033,
          "priority": 19,
          "result": {
            "brootid": 63755809,
            "logs": [
              "tasks/4050/139004050/state.log",
              "tasks/4050/139004050/root.log",
              "tasks/4050/139004050/build.log",
              "tasks/4050/139004050/dnf5.log",
              "tasks/4050/139004050/mock_output.log",
              "tasks/4050/139004050/hw_info.log",
              "tasks/4050/139004050/mock_config.log"
            ],
            "source": {
              "source": "git+https://src.fedoraproject.org/rpms/prusa-slicer.git#ddbac739fc9482082b06028e5606f74c06e1db07",
              "url": "git+https://src.fedoraproject.org/rpms/prusa-slicer.git#ddbac739fc9482082b06028e5606f74c06e1db07"
            },
            "srpm": "tasks/4050/139004050/prusa-slicer-2.9.4-1.fc44.src.rpm"
          },
          "start_time": 1763384977.0,
          "state": 2,
          "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=139004050",
          "waiting": null
        },
        {
          "arch": "x86_64",
          "awaited": false,
          "channel_id": 1,
          "children": [],
          "completion_time": 1763387377.0,
          "create_time": 1763385036.0,
          "host_id": 697,
          "host_name": "buildhw-x86-09.rdu3.fedoraproject.org",
          "id": 139004153,
          "label": "x86_64",
          "method": "buildArch",
          "owner": "spot",
          "parent": 139004033,
          "priority": 19,
          "result": {
            "brootid": 63755882,
            "logs": [
              "tasks/4153/139004153/mock_config.log",
              "tasks/4153/139004153/hw_info.log",
              "tasks/4153/139004153/root.log",
              "tasks/4153/139004153/mock_output.log",
              "tasks/4153/139004153/build.log",
              "tasks/4153/139004153/state.log",
              "tasks/4153/139004153/dnf5.log"
            ],
            "rpms": [
              "tasks/4153/139004153/prusa-slicer-debuginfo-2.9.4-1.fc44.x86_64.rpm",
              "tasks/4153/139004153/prusa-slicer-2.9.4-1.fc44.x86_64.rpm",
              "tasks/4153/139004153/prusa-slicer-debugsource-2.9.4-1.fc44.x86_64.rpm"
            ],
            "srpms": [
              "tasks/4153/139004153/prusa-slicer-2.9.4-1.fc44.src.rpm"
            ]
          },
          "start_time": 1763385094.0,
          "state": 2,
          "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=139004153",
          "waiting": null
        },
        {
          "arch": "aarch64",
          "awaited": false,
          "channel_id": 1,
          "children": [],
          "completion_time": 1763388901.0,
          "create_time": 1763385036.0,
          "host_id": 622,
          "host_name": "buildvm-a64-20.rdu3.fedoraproject.org",
          "id": 139004154,
          "label": "aarch64",
          "method": "buildArch",
          "owner": "spot",
          "parent": 139004033,
          "priority": 19,
          "result": {
            "brootid": 63755894,
            "logs": [
              "tasks/4154/139004154/state.log",
              "tasks/4154/139004154/mock_config.log",
              "tasks/4154/139004154/hw_info.log",
              "tasks/4154/139004154/root.log",
              "tasks/4154/139004154/mock_output.log",
              "tasks/4154/139004154/dnf5.log",
              "tasks/4154/139004154/build.log"
            ],
            "rpms": [
              "tasks/4154/139004154/prusa-slicer-debuginfo-2.9.4-1.fc44.aarch64.rpm",
              "tasks/4154/139004154/prusa-slicer-2.9.4-1.fc44.aarch64.rpm",
              "tasks/4154/139004154/prusa-slicer-debugsource-2.9.4-1.fc44.aarch64.rpm"
            ],
            "srpms": []
          },
          "start_time": 1763385097.0,
          "state": 2,
          "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=139004154",
          "waiting": null
        }
      ],
      "completion_time": 1763390521.0,
      "create_time": 1763384884.0,
      "host_id": 662,
      "host_name": "buildvm-a64-40.rdu3.fedoraproject.org",
      "id": 139004033,
      "label": null,
      "method": "build",
      "owner": "spot",
      "parent": null,
      "priority": 20,
      "request": [
        "git+https://src.fedoraproject.org/rpms/prusa-slicer.git#ddbac739fc9482082b06028e5606f74c06e1db07",
        "rawhide",
        {}
      ],
      "result": null,
      "start_time": 1763384912.0,
      "state": 3,
      "url": "https://koji.fedoraproject.org/koji/taskinfo?taskID=139004033",
      "waiting": true
    },
    "task_id": 139004033,
    "url": "https://koji.fedoraproject.org/koji/buildinfo?buildID=2860061",
    "version": "2.9.4"
  },
  "headers": {
    "fedora_messaging_rpm_prusa-slicer": true,
    "fedora_messaging_schema": "koji_fedoramessaging.build.BuildStateChangeV1",
    "fedora_messaging_schema_package": "koji_fedoramessaging_messages",
    "fedora_messaging_severity": 20,
    "fedora_messaging_user_spot": true,
    "priority": 0,
    "sent-at": "2025-11-17T14:42:02+00:00"
  },
  "id": "eb9af16c-7324-4140-bc99-1822915f359b",
  "priority": 0,
  "queue": null,
  "topic": "org.fedoraproject.prod.buildsys.build.state.change"
}
"""
    )
    msg = message.load_message(msg_dump)
    msg_str = str(msg)  # This must not crash
    assert msg_str.startswith("Package:    prusa-slicer-2.9.4-1.fc44\nStatus:     canceled")
