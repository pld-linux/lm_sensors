%define		_kernel_ver	%(grep UTS_RELEASE %{_kernelsrcdir}/include/linux/version.h 2>/dev/null | cut -d'"' -f2)
%define		_kernel24	%(echo %{_kernel_ver} | grep -q '2\.[012]\.' ; echo $?)
%define		smpstr		%{?_with_smp:smp}%{!?_with_smp:up}
%define		smp		%{?_with_smp:1}%{!?_with_smp:0}

Summary:	Hardware health monitoring
Summary(pl):	Monitor stanu sprzêtu
Name:		lm_sensors
Version:	2.5.5
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
BuildRequires:	flex >= 2.5.1
BuildRequires:	kernel-headers >= 2.3.0
Requires:	%{name}-modules = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description -l pl
Narzêdzie do monitorowania sprzêtu w systemach Linuxowych wyposa¿onych
w sprzêt monitoruj±cy, taki jak LM78 and LM75.

%package devel
Summary:	Header files for lm_sensors
Summary(pl):	Pliki nag³ówkowe dla lm_sensors
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for lm_sensors.

%description devel -l pl
Pliki nag³ówkowe dla lm_sensors.

%package static
Summary:	Static libraries for lm_sensors
Summary(pl):	Biblioteki statyczne dla lm_sensors
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Statis libraries for lm_sensors.

%description static -l pl
Biblioteki statyczne dla lm_sensors.

%package modules
Summary:	Kernel modules for various buses and monitor chips
Summary(pl):	Modu³y j±dra dla ró¿nego rodzaju sensorów
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Release:	%{release}@%{_kernel_ver}%{smpstr}
Prereq:		/sbin/depmod
Conflicts:	kernel < %{_kernel_ver}, kernel > %{_kernel_ver}
Conflicts:	kernel-%{?_with_smp:up}%{!?_with_smp:smp}

%description modules
Kernel modules for various buses and monitor chips.

%description -l pl
Modu³y j±dra dla ró¿nego rodzaju sensorów monitoruj±cych.

%prep
%setup -q
%patch0 -p1

%build
%if %{smp}
SMP="-D__KERNEL_SMP=1"
%endif
%{__make} \
	OPTS="%{rpmcflags} $SMP" \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=%{smp}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	ETCDIR=%{_sysconfdir} \
	MANDIR=%{_mandir} \
%if %{_kernel24}
	MODDIR=/lib/modules/%{_kernel_ver}/kernel/drivers/i2c
%else
	MODDIR=/lib/modules/%{_kernel_ver}/misc
%endif

gzip -9nf CHANGES README* BUGS CONTRIBUTORS TODO BACKGROUND
gzip -9nf doc/* || :

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post modules
/sbin/depmod -a

%postun modules
/sbin/depmod -a

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc {CHANGES,README*,BUGS,CONTRIBUTORS,TODO,BACKGROUND}.gz 
%doc doc/*.gz doc/busses doc/chips
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_sbindir}/sensors-detect
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config %{_sysconfdir}/sensors.conf
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc doc/developers doc/kernel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/sensors
%{_includedir}/linux/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsensors.a

%files modules
%defattr(644,root,root,755)
%if %{_kernel24}
/lib/modules/*/kernel/drivers/i2c/*
%else
/lib/modules/*/misc/*
%endif
