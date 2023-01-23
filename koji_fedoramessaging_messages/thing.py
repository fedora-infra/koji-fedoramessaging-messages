# Copyright (C) 2023  Red Hat, Inc.
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

from .base import SCHEMA_URL, kojifedoramessagingMessage, THING_SCHEMA


class NewThingV1(kojifedoramessagingMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by koji-fedoramessaging when a new thing is created.
    """

    topic = "koji-fedoramessaging.new"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a new thing is created",
        "type": "object",
        "properties": {"agent": {"type": "string"}, "thing": THING_SCHEMA},
        "required": ["agent", "thing"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "New Thing: {thing}\nBy: {agent}\n".format(
            thing=self.body["thing"]["name"],
            agent=self.body["agent"],
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return '{agent} created thing "{name}" ({id})'.format(
            agent=self.body["agent"],
            name=self.body["thing"]["name"],
            id=self.body["thing"]["id"],
        )
