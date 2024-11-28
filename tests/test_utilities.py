# SPDX-FileCopyrightText: 2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pytest

from koji_fedoramessaging_messages.utilities import date_to_string


@pytest.mark.parametrize(
    "timestamp,expected",
    [("2023-06-09T07:16:27.818161+00:00", "Fri, 09 Jun 2023 07:16:27 UTC"), (None, "")],
)
def test_date_to_string(timestamp, expected):
    assert date_to_string(timestamp) == expected
