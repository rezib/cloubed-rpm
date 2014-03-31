%define name cloubed
%define version 0.3
%define unmangled_version 0.3
%define release 1

Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Summary: Utility and library to easily setup virtual testbeds composed of several KVM virtual machines through libvirt
Group: Development/Libraries
Vendor: Rémi Palancher <remi@rezib.org>

License: LGPLv3
Source0: %{name}-%{unmangled_version}.tar.gz

Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch: noarch
BuildRequires: python-setuptools
# needs EPEL enable
BuildRequires: python-sphinx10

Requires: libvirt-python
Requires: python-yaml
Requires: python-argparse

%description
Soon.

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

# build and compress manpage
sphinx-1.0-build -N -b man doc/ doc/_build/man/
gzip doc/_build/man/%{name}.1

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed -O1 --root=%{buildroot}
install -D doc/_build/man/%{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz


%clean
rm -rf %{buildroot}

%files
%{python_sitelib}/*
%{_bindir}/cloubed
%doc %{_mandir}/man1/*

%changelog
* Mon Mar 31 2014 Rémi Palancher <remi@rezib.org> - 0.3-1
- hide clean_exit() from public API
- avoid _clean_exit() creates instance of Cloubed
- avoid nonexistent Configuration.get_file_path()
- add all needed internal method to return xml
- add xml action on script
- fix typo in installation part of README
- do not use _doc in StoragePool.create()
- add support for using existing bridge as network
- ignore useless exception when error in __del__()
- update the domain XML sample comment
- add abstract generic ConfigurationItem class
- new method to parse ip_host and netmask in YAML
- add method to parse dhcp parameters in YAML
- add method to parse pxe parameters in YAML
- add method to parse names in YAML
- new method to parse testbed name in YAML
- new method to parse items in YAML
- new method to parse global templates in YAML
- conf dict not Configuration attribute anymore
- new method to parse storage pool path in YAML
- make sure everything is a string in templates dict
- fix wrong exception name
- clean-up + default spice in __parse_graphics()
- new method to parse domains templates in YAML
- new methods to parse storage volumes in YAML
- fix string equality tests
- various clean-ups in domains parsing methods
- avoid tracking of coverage file in git
- first set of unit tests
- print additional information with cloubed status
- add new Utils module with utility functions
- add new utility getuser() and use it everywhere
- several modifications in setup.py
- move cli check_*() args checking functions
- updated logic to check coherency of optional args
- add new unit tests for CloubedArgumentParser class
- first version of the documentation
- fix parse_*() do not take argument
- add libvirt-python binding in install_requires
- check disks to overwrite in boot_vm()
- check networks to recreate in boot_vm()
- move API functions from cloubed.py to __init__.py
- launch event manager thread only if needed
- add API functions to get list of resources names
- ignore dirs created by setuptools in git
- add MANIFEST.in file to include doc and tests
- update installation instructions in documentation
- Cloubed release v0.3

* Tue Mar 27 2014 Rémi Palancher <remi@rezib.org> - 0.2-1
- initial RPM release
