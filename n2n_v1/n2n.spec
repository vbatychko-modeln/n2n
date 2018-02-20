Summary: N2N peer-to-peer virtual private network system.
Name: n2n
Version: 1.3
Release: 1
License: GPLv3
Vendor: ntop.org
Group: None
URL: http://www.ntop.org/n2n
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?systemd_requires}
BuildRequires: systemd

%description
N2N is a peer-to-peer virtual private network system. N2N uses the universal
TUNTAP interface to create TAP network interfaces to an encrypted virtual
LAN. Members of a community share a common encryption key which allows echange
of data. The supernode is used for peer discovery and initial packet relay
before direct peer-to-peer exchange is established.
Once direct packet exchange is established, the supernode is not required.

%prep

%setup -q

echo -e "\n *** Building ${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE} ***\n"

%build
make

%install
make PREFIX=${RPM_BUILD_ROOT}/usr install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
     /usr/bin/supernode
     /usr/sbin/edge
     /etc/sysconfig/n2n
     /usr/lib/systemd/system/n2n-edge.service
     /usr/lib/systemd/system/n2n-supernode.service
%doc /usr/share/man/man1/supernode.1.gz
%doc /usr/share/man/man8/edge.8.gz

%post
%systemd_post n2n-edge.service
%systemd_post n2n-supernode.service

%preun
%systemd_preun n2n-edge.service
%systemd_preun n2n-supernode.service

%postun
%systemd_postun_with_restart n2n-edge.service
%systemd_postun_with_restart n2n-supernode.service


%changelog
* Sat May  3 2008 Richard Andrews <andrews@ntop.org> - 
- Initial build.

