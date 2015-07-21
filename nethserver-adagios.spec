Name: nethserver-adagios
Version: 0.0.1
Release: 1%{?dist}
Summary: Conifigure Adagios
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: pnp4nagios
Requires: mk-livestatus
Requires: nagios
Requires: git
Requires: adagios
Requires: okconfig
Requires: python-setuptools
Requires: nagios-plugins-all

%description
Install and configure an Adagios instance on NethServer

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING

%changelog
* Tue Jul 21 2015 Davide Principi <davide.principi@nethesis.it>
- Initial version
