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


from fedora_messaging import message


SCHEMA_URL = "http://fedoraproject.org/message-schema/"


class KojiFedoraMessagingMessage(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by the koji fedora-messaging plugin.
    """

    @property
    def app_name(self):
        return "Koji"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/koji.png"

    @property
    def owner(self):
        return None

    @property
    def agent_name(self):
        # This seems wrong: actions on a package aren't always triggered by the package owner, no?
        # If we're not sure who initiated the action, it's better to have agent_name be None.
        # In any case, this seems like a dangerous default here.
        return self.owner

    @property
    def usernames(self):
        if self.agent_name:
            return [self.agent_name]
        else:
            return []

    def __str__(self):
        return self.summary
