
# conditional build
# _without_dist_kernel		without kernel for distributions

%define		_kernel_ver	%(grep UTS_RELEASE %{_kernelsrcdir}/include/linux/version.h 2>/dev/null | cut -d'"' -f2)
%define		_kernel_ver_str	%(echo %{_kernel_ver} | sed s/-/_/g)
%define		_rel 6

Summary:	Hardware health monitoring
Summary(pl):	Monitor stanu sprzêtu
Name:		lm_sensors
Version:	2.6.2
Release:	%{_rel}
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
Source1:	sensors.init
Source2:	sensors.sysconfig
Patch0:		%{name}-make.patch
URL:		http://www.netroedge.com/~lm78/
BuildRequires:	flex >= 2.5.1
BuildRequires:	bison
#BuildRequires:  i2c-devel >= 2.6.0
PreReq:		/sbin/chkconfig
PreReq:		/sbin/ldconfig
Requires:	%{name}-modules = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description -l pl
Narzêdzie do monitorowania sprzêtu w systemach Linuksowych
wyposa¿onych w sprzêt monitoruj±cy, taki jak LM78 lub LM75.

%package devel
Summary:	Header files for lm_sensors
Summary(pl):	Pliki nag³ówkowe dla lm_sensors
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
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
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static libraries for lm_sensors.

%description static -l pl
Biblioteki statyczne dla lm_sensors.

%package -n kernel-misc-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl):	Modu³y j±dra dla ró¿nego rodzaju sensorów
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Release:	%{_rel}@%{_kernel_ver_str}
Prereq:		/sbin/depmod
Requires:	i2c >= 2.6.0
%{?!_without_dist_kernel:Conflicts:	kernel < %{_kernel_ver}, kernel > %{_kernel_ver}}
%{?!_without_dist_kernel:Conflicts:	kernel-smp}
Obsoletes:	%{name}-modules
Obsoletes:	kernel-smp-misc-%{name}
Provides:	%{name}-modules = %{version}

%description -n kernel-misc-%{name}
Kernel modules for various buses and monitor chips.

%description -n kernel-misc-%{name} -l pl
Modu³y j±dra dla ró¿nego rodzaju sensorów monitoruj±cych.


%package -n kernel-smp-misc-%{name}
Summary:        Kernel modules for various buses and monitor chips
Summary(pl):    Modu³y j±dra dla ró¿nego rodzaju sensorów
Group:          Applications/System
Group(de):      Applikationen/System
Group(pl):      Aplikacje/System
Release:        %{_rel}@%{_kernel_ver_str}
Prereq:         /sbin/depmod
Requires:       i2c >= 2.6.0
%{?!_without_dist_kernel:Conflicts:     kernel < %{_kernel_ver}, kernel > %{_kernel_ver}}
%{?!_without_dist_kernel:Conflicts:     kernel-up}
Obsoletes:      %{name}-modules
Obsoletes:      kernel-misc-%{name}
Provides:       %{name}-modules = %{version}

%description -n kernel-smp-misc-%{name}
Kernel SMP modules for various buses and monitor chips.

%description -n kernel-smp-misc-%{name} -l pl
Modu³y j±dra SMP dla ró¿nego rodzaju sensorów monitoruj±cych.



%prep
%setup -q
%patch0 -p1

%build

#up
%{__make} \
	OPTS="%{rpmcflags}" \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=0

%{__make} install-kernel \
        MODDIR=kernel-up-modules
%{__make} install-kernel-busses \
        MODDIR=kernel-up-modules
%{__make} install-kernel-chips \
        MODDIR=kernel-up-modules

%{__make} clean

#smp
%{__make} \
        OPTS="%{rpmcflags} -D__KERNEL_SMP=1" \
        LINUX=/dev/null \
        LINUX_HEADERS=%{_kernelsrcdir}/include \
        I2C_HEADERS=%{_kernelsrcdir}/include \
        SMP=1
					
%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	ETCDIR=%{_sysconfdir} \
	MANDIR=%{_mandir} \
	MODDIR=/lib/modules/%{_kernel_ver}smp/misc

install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man8
install prog/sensord/sensord $RPM_BUILD_ROOT%{_sbindir}
install prog/sensord/sensord.8 $RPM_BUILD_ROOT%{_mandir}/man8

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/sensors
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/sensors

install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc
install kernel-up-modules/* $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc 

gzip -9nf BACKGROUND BUGS CHANGES README README.thinkpad TODO
find doc -type f ! -name \*.\* -a ! -name \*ticket | xargs gzip -9nf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add sensors
if [ -f /var/lock/subsys/sensors ]; then
	/etc/rc.d/init.d/sensors restart >&2
else
	echo "You have to configure sensors modules."
	echo "Please edit /etc/sysconfig/sensors file according to your hardware."
	echo
	echo "Run \"/etc/rc.d/init.d/sensors start\" to start sensors daemon." >&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/sensors ]; then
		/etc/rc.d/init.d/sensors stop >&2
	fi
	/sbin/chkconfig --del sensors
fi

%postun	-p /sbin/ldconfig

%post -n kernel-misc-%{name}
/sbin/depmod -a

%post -n kernel-smp-misc-%{name}
/sbin/depmod -a

%postun -n kernel-misc-%{name}
/sbin/depmod -a

%postun -n kernel-smp-misc-%{name}
/sbin/depmod -a


%files 
%defattr(644,root,root,755)
%doc *.gz 
%doc doc/*.gz doc/*.html doc/busses doc/chips
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_sbindir}/sensors-detect
%attr(754,root,root) %{_sbindir}/sensord
%attr(754,root,root) /etc/rc.d/init.d/sensors
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sensors.conf
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/sensors
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%doc doc/developers doc/kernel
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/sensors
%{_includedir}/linux/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsensors.a

%files -n kernel-misc-%{name}
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-misc-%{name}
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*
