%global opinkerfi_misc_commit 4d68cca3ce76ee3bc76edd5d3e810e9b2bb221aa

Name: nethserver-adagios
Version: 1.0.3
Release: 1%{?dist}
Summary: Conifigure Adagios
Source0: %{name}-%{version}.tar.gz
Source1: https://github.com/opinkerfi/misc/archive/%{opinkerfi_misc_commit}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: nethserver-xinetd
Requires: nethserver-httpd
Requires: nethserver-directory
Requires: mod_ldap
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

sed -i '\| /etc/nagios/conf.d| d' %{name}-%{version}-filelist
sed -i '\| /etc/nagios$| d' %{name}-%{version}-filelist

mkdir -p %{buildroot}/usr/share/okconfig/client/windows/nsclient
cp -av --no-preserve=mode %{_builddir}/misc-%{opinkerfi_misc_commit}/nsclient/src/* %{buildroot}/usr/share/okconfig/client/windows/nsclient

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
/usr/share/okconfig/client/windows/nsclient
%attr(0600,nagios,nagios) %config(noreplace) /etc/nagios/conf.d/admin-contact.cfg
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Nov 12 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1
- Adagios: can't change admin mail address for notification - Bug #3316 [NethServer]

* Wed Sep 16 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Adagios and OCS Inventory dashboard links broken - Bug #3256 [NethServer]

* Mon Sep 14 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.1-2
- Hotfix: limit nagios recursive chown to /etc/nagios/.git - Enhancement #3254 [NethServer]

* Mon Sep 14 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Adagios: the admin contact is not defined  - Bug #3255 [NethServer]
- Execute initial commit of Nagios configuration - Enhancement #3254 [NethServer]
- OCS Inventory LDAP authentication - Enhancement #3250 [NethServer]

* Tue Aug 25 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- Initial adagios package - Feature #3229 [NethServer]

* Tue Jul 21 2015 Davide Principi <davide.principi@nethesis.it>
- Initial version
