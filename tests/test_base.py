# SPDX-FileCopyrightText: 2020-2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

from koji_fedoramessaging_messages.repo import DoneV1


def test_base():
    msg = DoneV1(
        body={
            "instance": "primary",
            "repo_id": 1409150,
            "tag": "module-jmc-latest-3220200311144307-089fddd9-build",
            "tag_id": 20164,
        }
    )
    assert msg.app_name == "Koji"
    assert msg.app_icon == "https://apps.fedoraproject.org/img/icons/koji.png"
    assert msg.agent_name is None
