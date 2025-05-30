# koji-fedoramessaging messages

A schema package for [koji-fedoramessaging](http://github.com/fedora-infra/koji-fedoramessaging).

See the [detailed documentation](https://fedora-messaging.readthedocs.io/en/latest/messages.html) on packaging your schemas.


## Rebuilding for Fedora Infra

At the moment this package is not in Fedora. To build a RPM for Fedora Infra, follow the following steps:

- checkout the latest tag: `git checkout v1.2.6`
- build the SRPM with Packit: `packit srpm --no-update-release`
- build the RPM in koji: `koji build f42-infra python-koji-fedoramessaging-messages-1.2.6-1.fc42.src.rpm`
- move the RPM to the production tag: `koji move f42-infra-stg f42-infra python-koji-fedoramessaging-messages-1.2.6-1.fc42`
