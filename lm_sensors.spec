Summary:	Hardware health monitoring
Summary(pl):	Monitor stanu sprzêtu
Name:		lm_sensors
Version:	2.3.4
Release:	1
Copyright:      GPL
Group:          Utilities/System
Group(pl):      Narzêdzia/System
Source0:	http://www.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
Patch0:		lm_sensors-DESTDIR.patch
Patch1:		lm_sensors-opts.patch
Prereq:		/sbin/depmod
Requires:       %{name}-modules = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sysconfdir	/etc

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description -l pl
Narzêdzie do monitorowania sprzêtu w systemach Linuxowych wyposa¿onych
w sprzêt monitoruj±cy, taki jak LM78 and LM75.

%package devel
Summary:        Header files for lm_sensors
Summary(pl):	Pliki nag³ówkowe dla lm_sensors
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:       %{name} = %{version}

%description devel
Header files for lm_sensors.

%description devel -l pl
Pliki nag³ówkowe dla lm_sensors.

%package static
Summary:	Static libraries for lm_sensors
Summary(pl):	Biblioteki statyczne dla lm_sensors
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:       %{name}-devel = %{version}

%description static
Statis libraries for lm_sensors.

%description static -l pl
Biblioteki statyczne dla lm_sensors.

%package modules
Summary: 	Kernel modules for various buses and monitor chips
Summary(pl):	Modu³y j±dra dla ró¿nego rodzaju sensorów
Group: 		Utilities/System
Group(pl):      Narzêdzia/System

%description modules
Kernel modules for various buses and monitor chips.

%description -l pl
Modu³y j±dra dla ró¿nego rodzaju sensorów monitoruj±cych.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
make OPTS="$RPM_OPT_FLAGS" 

%install
rm -fr $RPM_BUILD_ROOT

REL=`grep UTS_RELEASE /usr/src/linux/include/linux/version.h 2>/dev/null | cut -d\" -f2`

make	install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	ETCDIR=%{_sysconfdir} \
	MANDIR=%{_mandir} \
	MODDIR=/lib/modules/$REL/misc

strip $RPM_BUILD_ROOT%{_bindir}/*
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[135]/* \
	CHANGES README* BUGS CONTRIBUTORS TODO BACKGROUND
gzip -9nrf doc/*

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
%doc {CHANGES,README*,BUGS,CONTRIBUTORS,TODO,BACKGROUND}.gz 
%doc doc/*.gz doc/busses doc/chips
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config %{_sysconfdir}/sensors.conf
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%doc doc/developers doc/kernel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so.0
%{_includedir}/sensors
%{_includedir}/linux/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsensors.a

%files modules
%defattr(644,root,root,755)
/lib/modules/*/misc/*
