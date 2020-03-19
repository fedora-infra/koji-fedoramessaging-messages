#!/usr/bin/python3
# Copyright (C) 2020 Red Hat, Inc.
#
# This file was copied from Bodhi
# (https://github.com/fedora-infra/bodhi/blob/5.1.1/docs/generate_json_schema).
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""Generate JSON schema RST files."""

import json
import os

from koji_fedmsg_plugin.messages import build, package, repo, rpm, tag, task


DOCS_DIR = os.path.dirname(os.path.realpath(__file__))


for module in (build, package, repo, rpm, tag, task):
    with open(f"{DOCS_DIR}/generated/{module.__name__.split('.')[-1]}.rst", 'w') as rst:
        for attr in dir(module):
            attr = getattr(module, attr)
            if hasattr(attr, 'body_schema') and hasattr(attr, 'topic') and attr.topic:
                indented_json = json.dumps(attr.body_schema, indent=4).replace('\n', '\n    ')
                rst.write(f"{attr.topic}\n{'-'*len(attr.topic)}\n::"
                          f'\n\n    {indented_json}\n\n')
