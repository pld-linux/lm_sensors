# conditional build
# _without_dist_kernel		without kernel for distributions
%include        /usr/lib/rpm/macros.perl
%define         _rel 0.9

Summary:	Hardware health monitoring
Summary(pl):	Monitor stanu sprzêtu
Summary(pt_BR):	Ferramentas para monitoração do hardware
Summary(ru):	õÔÉÌÉÔÙ ÄÌÑ ÍÏÎÉÔÏÒÉÎÇÁ ÁÐÐÁÒÁÔÕÒÙ
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ ÍÏÎ¦ÔÏÒÉÎÇÕ ÁÐÁÒÁÔÕÒÉ
Name:		lm_sensors
Version:	2.6.4
Release:	%{_rel}
License:	GPL
Group:		Applications/System
Source0:	http://secure.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
Source1:	sensors.init
Source2:	sensors.sysconfig
Patch0:		%{name}-make.patch
URL:		http://www.lm-sensors.nu/
BuildRequires:	bison
BuildRequires:	flex >= 2.5.1
BuildRequires:	perl-modules >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rrdtool-devel
%{!?_without_dist_kernel:BuildRequires:	i2c-devel >= 2.6.0}
PreReq:		/sbin/chkconfig
PreReq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	liblm_sensors1

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description -l pl
Narzêdzie do monitorowania sprzêtu w systemach Linuksowych
wyposa¿onych w sprzêt monitoruj±cy, taki jak LM78 lub LM75.

%description -l pt_BR
Ferramentas para monitoração do hardware. Contém uma coleção de
módulos para acesso genérico ao barramento SMBus e monitoração de
hardware.

%description -l ru
ðÁËÅÔ lm_sensors ÓÏÄÅÒÖÉÔ ÎÁÂÏÒ ÍÏÄÕÌÅÊ ÄÌÑ ÓÔÁÎÄÁÒÔÎÏÇÏ ÄÏÓÔÕÐÁ Ë
SMBus É ÍÏÎÉÔÏÒÉÎÇÁ. ÷îéíáîéå: ÄÌÑ ÜÔÏÇÏ ÎÅÏÂÈÏÄÉÍÁ ÓÐÅÃÉÁÌØÎÁÑ
ÐÏÄÄÅÒÖËÁ, ÏÔÓÕÔÓÔ×ÕÀÝÁÑ × ÓÔÁÎÄÁÒÔÎÙÈ ÓÔÁÒÙÈ ÑÄÒÁÈ 2.2.XX !

%description -l uk
ðÁËÅÔ lm_sensors Í¦ÓÔÉÔØ ÎÁÂ¦Ò ÍÏÄÕÌ¦× ÄÌÑ ÓÔÁÎÄÁÒÔÎÏÇÏ ÄÏÓÔÕÐÕ ÄÏ
SMBus ÔÁ ÍÏÎ¦ÔÏÒÉÎÇÕ. õ÷áçá: ÄÌÑ ÃØÏÇÏ ÐÏÔÒ¦ÂÎÁ ÓÐÅÃ¦ÁÌØÎÁ Ð¦ÄÔÒÉÍËÁ,
ÑËÁ ×¦ÄÓÕÔÎÑ Õ ÓÔÁÎÄÁÒÔÎÉÈ ÓÔÁÒÉÈ ÑÄÒÁÈ 2.2.XX !

%package sensord
Summary:	Sensord daemon
Summary(pl):	Demon sensord
Group:		Daemon
Requires:	%{name} = %{version}

%description sensord
Sensord daemon.

%description sensord -l pl
Demon sensord.

%package devel
Summary:	Header files for lm_sensors
Summary(pl):	Pliki nag³ówkowe dla lm_sensors
Summary(pt_BR):	Arquivos necessários ao desenvolvimento de programas que usem o lm_sensors
Summary(ru):	æÁÊÌÙ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ lm_sensors
Summary(uk):	æÁÊÌÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ ÐÒÏÇÒÁÍ, ÑË¦ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ lm_sensors
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	liblm_sensors1-devel

%description devel
Header files for lm_sensors.

%description devel -l pl
Pliki nag³ówkowe dla lm_sensors.

%description devel -l pt_BR
Arquivos necessários ao desenvolvimento de programas que usem o
lm_sensors.

%description devel -l ru
ðÁËÅÔ lm_sensors-devel ×ËÌÀÞÁÅÔ ÈÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ
ÐÏÓÔÒÏÅÎÉÑ ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ ÄÁÎÎÙÅ ÓÅÎÓÏÒÏ×.

%description devel -l uk
ðÁËÅÔ lm_sensors-devel Í¦ÓÔÉÔØ ÈÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ
ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ, ÑË¦ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ ÄÁÎ¦ ÓÅÎÓÏÒ¦×.

%package static
Summary:	Static libraries for lm_sensors
Summary(pl):	Biblioteki statyczne dla lm_sensors
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com lm_sensors
Summary(ru):	óÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ lm_sensors
Summary(uk):	óÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÐÒÏÇÒÁÍ, ÑË¦ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ lm_sensors
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for lm_sensors.

%description static -l pl
Biblioteki statyczne dla lm_sensors.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com lm_sensors

%description static -l ru
ðÁËÅÔ lm_sensors-static ×ËÌÀÞÁÅÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ
ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ ÄÁÎÎÙÅ ÓÅÎÓÏÒÏ×.

%description static -l uk
ðÁËÅÔ lm_sensors-static Í¦ÓÔÉÔØ ÓÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ
ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ, ÑË¦ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ ÄÁÎ¦ ÓÅÎÓÏÒ¦×.

%package -n kernel-misc-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl):	Modu³y j±dra dla ró¿nego rodzaju sensorów
Group:		Applications/System
Release:	%{_rel}@%{_kernel_ver_str}
Prereq:		/sbin/depmod
%{!?_without_dist_kernel:%requires_releq_kernel_up}
%{!?_without_dist_kernel:Requires:	i2c >= 2.6.0}
Provides:	%{name}-modules = %{version}
Obsoletes:	%{name}-modules

%description -n kernel-misc-%{name}
Kernel modules for various buses and monitor chips.

%description -n kernel-misc-%{name} -l pl
Modu³y j±dra dla ró¿nego rodzaju sensorów monitoruj±cych.

%package -n kernel-smp-misc-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl):	Modu³y j±dra dla ró¿nego rodzaju sensorów
Group:		Applications/System
Release:	%{_rel}@%{_kernel_ver_str}
Prereq:		/sbin/depmod
%{!?_without_dist_kernel:%requires_releq_kernel_smp}
%{!?_without_dist_kernel:Requires:	i2c >= 2.6.0}
Provides:	%{name}-modules = %{version}
Obsoletes:	%{name}-modules

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
        MODPREF=kernel-up-modules
%{__make} install-kernel-chips \
        MODPREF=kernel-up-modules

%{__make} clean

#smp
%{__make} \
	OPTS="%{rpmcflags} -D__KERNEL_SMP=1" \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	PROG_EXTRA:="sensord dump" \
	SMP=1

cd prog/eepromer
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig},/lib/modules/%{_kernel_ver}/misc}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	ETCDIR=%{_sysconfdir} \
	MANDIR=%{_mandir} \
	PROG_EXTRA:="sensord dump" \
	MODDIR=/lib/modules/%{_kernel_ver}smp/misc \
	MODPREF=/lib/modules/%{_kernel_ver}smp

install prog/eepromer/{eeprom,eepromer} $RPM_BUILD_ROOT%{_sbindir}
install prog/dump/{i2c{dump,set},isadump} $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/sensors
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/sensors

install kernel-up-modules/misc/* $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc

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
%doc BACKGROUND BUGS CHANGES README README.thinkpad TODO doc/{busses,chips}
%doc doc/{FAQ,donations,fan-divisors,progs,temperature-sensors,*html,vid}
%doc prog/{config,daemon,eeprom,eepromer/README*,matorb,maxilife,xeon}
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_sbindir}/sensors-detect
%attr(755,root,root) %{_sbindir}/eeprom*
%attr(755,root,root) %{_sbindir}/i2c*
%attr(755,root,root) %{_sbindir}/isadump
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sensors.conf
%{_mandir}/man1/*
%{_mandir}/man5/*

%files sensord 
%defattr(644,root,root,755)
%attr(754,root,root) %{_sbindir}/sensord
%attr(754,root,root) /etc/rc.d/init.d/sensors
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/sensors
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%doc doc/{developers,kernel}
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
