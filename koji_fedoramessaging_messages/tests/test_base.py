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
