#!/bin/sh

# SPDX-FileCopyrightText: 2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

set -e

LANG=en_US.UTF-8
SPEC=python-koji-fedoramessaging-messages.spec
VERSION=$(poetry version -s)
AUTHOR=$(git log -1 --format="%an <%ae>")
CHANGELOG="* `date +"%a %b %d %Y"` ${AUTHOR} - ${VERSION}-1\n- Version ${VERSION}"

sed -e '
    s/@@VERSION@@/'${VERSION}'/g;
    $a\
'"${CHANGELOG}"'
    ' ${SPEC}.in > ${SPEC}
