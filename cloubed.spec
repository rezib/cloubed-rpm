%define name cloubed
%define version 0.4
%define unmangled_version 0.4
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
* Sun Dec 21 2014 Rémi Palancher <remi@rezib.org> - 0.4-1
- New upstream release 0.4

* Mon Mar 31 2014 Rémi Palancher <remi@rezib.org> - 0.3-1
- New upstream release 0.3

* Tue Mar 27 2014 Rémi Palancher <remi@rezib.org> - 0.2-1
- initial RPM release
