# Copyright © 2020 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from koji_fedoramessaging_messages.build import BuildStateChangeV1


def test_base():

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
    assert msg.app_name == "koji"
    assert msg.app_icon == "https://apps.fedoraproject.org/img/icons/koji.png"
