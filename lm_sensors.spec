Summary:	Hardware health monitoring
Summary(pl):	Monitor zdrowia sprzêtu
Name:		lm_sensors
Version:	2.3.3
Release:	2
Group:          Utilities/System
Group(pl):      Narzêdzia/System
Source0:	http://www.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
Copyright:	GPL
Prereq:		/sbin/depmod -a
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description -l pl
Narzêdzie do monitorowania sprzêtu w systemach Linuxowych wyposa¿onych
w sprzêt monitoruj±cy, taki jak LM78 and LM75.

%package devel
Summary:        Header files for lm_sensors
Summary(pl):	Pliki nag³ówkowe dla lm_sensors
Group:          Develompent/Libraries
Group(pl):      Programowanie/Biblioteki

%description devel
Header files for lm_sensors.

%description devel -l pl
Pliki nag³ówkowe dla lm_sensors.

%package static
Summary:	Static libraries for lm_sensors
Summary(pl):	Biblioteki statyczne dla lm_sensors
Group:          Develompent/Libraries
Group(pl):      Programowanie/Biblioteki

%description static
Statis libraries for lm_sensors.

%description static -l pl
Biblioteki statyczne dla lm_sensors.

%package modules
Summary: 	Kernel modules for various buses and monitor chips.
Group: 		Utilities/System
Group(pl):      Narzêdzia/System

%description modules
Kernel modules for various buses and monitor chips.

%description -l pl
Modu³y j±dra dla ró¿nych chipów monitoruj±cych.

%prep
%setup -q


%build
make 

%install
rm -fr $RPM_BUILD_ROOT

REL=`grep UTS_RELEASE /usr/src/linux/include/linux/version.h 2>/dev/null | cut -d\" -f2`

make	install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir} \
	MODDIR=$RPM_BUILD_ROOT/lib/modules/$REL/misc

gzip -9nf CHANGES README* doc/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post modules
/sbin/depmod -a

%postun modules
/sbin/depmod -a

%clean
rm -fr $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc {CHANGES,README*}.gz doc
%config /etc/sensors.conf
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so.0
%{_includedir}/sensors
%{_includedir}/linux/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsensors.a

%files modules
%defattr(644,root,root,755)
/lib/modules/*/misc/*
