Summary:	Hardware health monitoring
Name:		lm_sensors
Version:	2.3.0
Release:	1
Source0:	http://www.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
Copyright:	GPL
Group:		Base/Kernel
Group(pl):	Bazowe/J±dro
Prereq:		/sbin/depmod -a
BuildRoot:	/tmp/%{name}-%{version}-root

%package modules
Summary: Kernel modules for various buses and monitor chips.
Version: %{modversion}
Group: Utilities/System

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description modules
Kernel modules for various busses and monitor chips.

%prep
%setup -q

%build
make 

%install
rm -fr $RPM_BUILD_ROOT
make	install \
	PREFIX=$RPM_BUILD_ROOT/usr \
	ETCDIR=$RPM_BUILD_ROOT/etc \
	MODDIR=$RPM_BUILD_ROOT/lib/modules/%{kernel}/misc

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post modules
/sbin/depmod -a

%postun modules
/sbin/depmod -a

%clean
rm -fr $RPM_BUILD_ROOT

%files 
%config /etc/sensors.conf
%doc CHANGES INSTALL README README.directories doc
%attr(644,root,root) %{_libdir}/libsensors.a
%attr(755,root,root) %{_libdir}/libsensors.so
%attr(755,root,root) %{_libdir}/libsensors.so.0
%attr(755,root,root) %{_libdir}/libsensors.so.0.0.2
%attr(755,root,root) %{_bindir}/sensors
%{_includedir}/sensors
%{_includedir}/linux/*

%files modules
/lib/modules/%{kernel}/misc/*

%changelog
* Sun Apr 25 1999  Ian Macdonald <ianmacd@xs4all.nl>
- compiled for kernel 2.2.6
- hyphen changed to underscore in version number to satisfy RPM 3.0

* Mon Apr  5 1999  Ian Macdonald <ianmacd@xs4all.nl>
- compiled for kernel 2.2.5

* Wed Mar 24 1999  Ian Macdonald <ianmacd@xs4all.nl>
- compiled for kernel 2.2.4

* Tue Mar  8 1999  Ian Macdonald <ianmacd@xs4all.nl>
- compiled for kernel 2.2.3

* Fri Feb 26 1999  Ian Macdonald <ianmacd@xs4all.nl>
- updated to lm_sensors 2.2.2 and compiled for kernel 2.2.2
- added /etc/sensors.conf
- added %post and %postun scripts
