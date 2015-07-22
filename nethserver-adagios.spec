%global opinkerfi_misc_commit 4d68cca3ce76ee3bc76edd5d3e810e9b2bb221aa

Name: nethserver-adagios
Version: 0.0.1
Release: 1%{?dist}
Summary: Conifigure Adagios
Source0: %{name}-%{version}.tar.gz
Source1: https://github.com/opinkerfi/misc/archive/%{opinkerfi_misc_commit}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: nethserver-xinetd
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
%setup -T -b 1 -n misc-%{opinkerfi_misc_commit}
%setup -D

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

mkdir -p %{buildroot}/usr/share/okconfig/client/windows/nsclient
cp -av --no-preserve=mode %{_builddir}/misc-%{opinkerfi_misc_commit}/nsclient/src/* %{buildroot}/usr/share/okconfig/client/windows/nsclient

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
/usr/share/okconfig/client/windows/nsclient

%changelog
* Tue Jul 21 2015 Davide Principi <davide.principi@nethesis.it>
- Initial version
