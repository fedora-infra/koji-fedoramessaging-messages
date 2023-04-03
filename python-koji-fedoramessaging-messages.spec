# Created by pyp2rpm-3.3.8
%global pypi_name koji-fedoramessaging-messages
%global pypi_version 1.0.6

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A schema package for messages sent by the koji-fedoramessaging plugin

License:        None
URL:            https://github.com/fedora-infra/koji-fedoramessaging-messages
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(fedora-messaging) >= 3.0.1
BuildRequires:  python3dist(setuptools)

%description
 koji-fedoramessaging messagesA schema package for [koji-fedoramessaging]( the
[detailed documentation]( on packaging your schemas.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(fedora-messaging) >= 3.0.1
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 koji-fedoramessaging messagesA schema package for [koji-fedoramessaging]( the
[detailed documentation]( on packaging your schemas.


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/koji_fedoramessaging_messages
%{python3_sitelib}/koji_fedoramessaging_messages-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 03 2023 Aurelien Bompard <abompard@fedoraproject.org> - 1.0.6-1
- Version 1.0.6

* Thu Feb 02 2023 Ryan Lerch <rlerch@redhat.com> - 1.0.4-1
- Initial package.
