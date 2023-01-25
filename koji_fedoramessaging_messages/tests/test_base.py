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
    msg = BuildStateChangeV1(body={})
    assert msg.app_name == "koji"
    assert msg.app_icon == "https://apps.fedoraproject.org/img/icons/koji.png"
    assert msg.agent_name is None
