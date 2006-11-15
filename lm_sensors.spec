# TODO
# - unpackaged:
#   /usr/sbin/fancontrol.pl (isn't that the same as sh fancontrol script?)
# - a big trigger warning how to use fancontrol and to init it first
#
%define		cmodule		%{_sysconfdir}/sysconfig/sensors_modules
%define		cdaemon		%{_sysconfdir}/sysconfig/sensors
%define		smodule		%{_sysconfdir}/rc.d/init.d/sensors_modules
%define		sdaemon		%{_sysconfdir}/rc.d/init.d/sensors

%include	/usr/lib/rpm/macros.perl
Summary:	Hardware health monitoring
Summary(pl):	Monitor stanu sprzЙtu
Summary(pt_BR):	Ferramentas para monitoraГЦo do hardware
Summary(ru):	Утилиты для мониторинга аппаратуры
Summary(uk):	Утил╕ти для мон╕торингу апаратури
Name:		lm_sensors
Version:	2.10.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.lm-sensors.org/lm-sensors/releases/%{name}-%{version}.tar.gz
# Source0-md5:	cdc857b78e813b88cbf8be92441aa299
Source1:	sensors.init
Source2:	sensors.sysconfig
Source3:	fancontrol.init
Source4:	fancontrol.sysconfig
Source5:	sensors.sh
Source6:	sensors_modules.init
Source7:	sensors_modules.sysconfig
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
Patch2:		%{name}-iconv-in-libc.patch
Patch3:		%{name}-sensors-detect-PATH.patch
URL:		http://www.lm-sensors.nu/
BuildRequires:	bison
BuildRequires:	flex >= 2.5.1
BuildRequires:	perl-modules >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rrdtool-devel >= 1.2.10
BuildRequires:	sysfsutils-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dev >= 2.9.0-13
Requires:	dmidecode
Requires:	%{name}-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description -l pl
NarzЙdzie do monitorowania sprzЙtu w systemach linuksowych
wyposa©onych w sprzЙt monitoruj╠cy, taki jak LM78 lub LM75.

%description -l pt_BR
Ferramentas para monitoraГЦo do hardware. ContИm uma coleГЦo de
mСdulos para acesso genИrico ao barramento SMBus e monitoraГЦo de
hardware.

%description -l ru
Пакет lm_sensors содержит набор модулей для стандартного доступа к
SMBus и мониторинга. ВНИМАНИЕ: для этого необходима специальная
поддержка, отсутствующая в стандартных старых ядрах 2.2.XX!

%description -l uk
Пакет lm_sensors м╕стить наб╕р модул╕в для стандартного доступу до
SMBus та мон╕торингу. УВАГА: для цього потр╕бна спец╕альна п╕дтримка,
яка в╕дсутня у стандартних старих ядрах 2.2.XX!

%package libs
Summary:	lm_sensors library
Summary(pl):	Biblioteka lm_sensors
Group:		Libraries
Obsoletes:	liblm_sensors1
Conflicts:	lm_sensors <= 2.9.2-2

%description libs
lm_sensors library.

%description libs -l pl
Biblioteka lm_sensors.

%package devel
Summary:	Header files for lm_sensors
Summary(pl):	Pliki nagЁСwkowe dla lm_sensors
Summary(pt_BR):	Arquivos necessАrios ao desenvolvimento de programas que usem o lm_sensors
Summary(ru):	Файлы разработчика для программ, использующих lm_sensors
Summary(uk):	Файли програм╕ста для програм, як╕ використовують lm_sensors
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	liblm_sensors1-devel

%description devel
Header files for lm_sensors.

%description devel -l pl
Pliki nagЁСwkowe dla lm_sensors.

%description devel -l pt_BR
Arquivos necessАrios ao desenvolvimento de programas que usem o
lm_sensors.

%description devel -l ru
Пакет lm_sensors-devel включает хедеры и библиотеки, необходимые для
построения программ, использующих данные сенсоров.

%description devel -l uk
Пакет lm_sensors-devel м╕стить хедери та б╕бл╕отеки, необх╕дн╕ для
побудови програм, як╕ використовують дан╕ сенсор╕в.

%package static
Summary:	Static libraries for lm_sensors
Summary(pl):	Biblioteki statyczne dla lm_sensors
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com lm_sensors
Summary(ru):	Статическая библиотека для программ, использующих lm_sensors
Summary(uk):	Статична б╕бл╕отека для програм, як╕ використовують lm_sensors
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for lm_sensors.

%description static -l pl
Biblioteki statyczne dla lm_sensors.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com lm_sensors

%description static -l ru
Пакет lm_sensors-static включает статические библиотеки, необходимые
для построения программ, использующих данные сенсоров.

%description static -l uk
Пакет lm_sensors-static м╕стить статичн╕ б╕бл╕отеки, необх╕дн╕ для
побудови програм, як╕ використовують дан╕ сенсор╕в.

%package config-default
Summary:	Sensors configuration files
Summary(pl):	Pliki konfiguracyjne lm_sensors
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-config

%description config-default
Default configuration files for lm_sensors.

%package sensord
Summary:	Sensord daemon
Summary(pl):	Demon sensord
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-config
Requires:	rc-scripts

%description sensord
Sensord daemon.

%description sensord -l pl
Demon sensord.

%package fancontrol
Summary:	Fancontrol daemon
Summary(pl):	Demon sterowania wiatraczkami
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-sensord = %{version}-%{release}
Requires:	rc-scripts

%description fancontrol
Fancontrol daemon monitors current temperature of the computer and
adjusts fans speed acordingly.

It is crucial to correctly configure this daemon (via running service
fancontrol init) and ensuring, that the temperature levels are set not
to burn the insides of the computer!

%description fancontrol -l pl
Demon fancontrol monitoruje obecn╠ temperaturЙ komputera i ustawia
odpowiednio prЙdko╤Ф wiatrakСw.

Kluczowym jest, aby poprawnie skonfigurowaФ tego demona (poprzez
uruchomienie service fancontrol init) oraz upewniФ siЙ, ©e progi
temperatury s╠ ustawione poprawnie, by nie spaliФ wnЙtrza komputera!

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} user \
	CC="%{__cc}" \
	OPTS="%{rpmcflags}" \
	LIBDIR=%{_libdir} \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=/usr/include \
	PROG_EXTRA:="sensord" \
	SYSFS_SUPPORT:=1

%{__make} -C prog/eepromer \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I../../kernel/include"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig}

%{__make} user_install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	ETCDIR=%{_sysconfdir} \
	LIBDIR=%{_libdir} \
	MANDIR=%{_mandir} \
	PROG_EXTRA:="sensord" \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=/usr/include

install prog/eepromer/{eeprom,eepromer}	$RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/sensors
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/sensors
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/fancontrol
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/fancontrol
install %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/sensors_modules
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/sensors_modules

# i2c API for userspace - included in glibc-kernel-headers
rm -f $RPM_BUILD_ROOT%{_includedir}/linux/i2c-dev.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post
if [ -f "%{cmodule}" ]; then
	/sbin/chkconfig --add sensors_modules
	%service sensors_modules restart "sensors modules"
	if [ -f "%{sdaemon}" ]; then
		/sbin/chkconfig --add sensors
		%service sensors restart "sensors deamon"
	fi
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f "%{sdaemon}" ]; then
		%service sensors stop
		/sbin/chkconfig --del sensors
	fi
	%service sensors_modules stop
	/sbin/chkconfig --del sensors_modules
fi

%post config-default
if [ "$1" = 1 ]; then
cat << EOF
 *********************************************************************
 *                                                                   *
 *  NOTE:                                                            *
 *  You have to configure sensors to match your motherboard sensors  *
 *  in  /etc/sensors.conf  and  /etc/sysconfig/sensors_modules. Use  *
 *  sensors-detect script which  can  help you find proper modules.  *
 *                                                                   *
 *********************************************************************
EOF
fi
if [ -f "%{smodule}" ]; then
	/sbin/chkconfig --add sensors_modules
	%service sensors_modules restart "sensors modules"
fi
if [ -f "%{sdaemon}" ]; then
	/sbin/chkconfig --add sensors
	%service sensors restart "sensors daemon"
fi

%preun config-default
if [ "$1" = "0" ]; then
	if [ -f "%{sdaemon}" ]; then
		%service sensors stop
		/sbin/chkconfig --del sensors
	fi
	if [ -f "%{smodule}" ]; then
		%service sensors_modules stop
		/sbin/chkconfig --del sensors_modules
	fi
fi

%post sensord
if [ -f "%{cmodule}" ]; then
	/sbin/chkconfig --add sensors
	%service sensors restart "sensors daemon"
fi

%preun sensord
if [ "$1" = "0" ]; then
	%service sensors stop
	/sbin/chkconfig --del sensors
fi

%post fancontrol
if [ "$1" = 1 ]; then
	echo "You have to configure fancontrol by running service fancontrol init first."
fi
/sbin/chkconfig --add fancontrol
%service fancontrol restart "fancontrol daemon"

%preun fancontrol
if [ "$1" = "0" ]; then
	%service fancontrol stop
	/sbin/chkconfig --del fancontrol
fi

%files
%defattr(644,root,root,755)
%doc BACKGROUND BUGS CHANGES README README.thinkpad TODO doc/{busses,chips}
%doc doc/{FAQ,donations,fan-divisors,progs,temperature-sensors,*html,vid}
%doc prog/{config,daemon,eepromer/README*,matorb,maxilife}
%attr(755,root,root) %{_bindir}/ddcmon
%attr(755,root,root) %{_bindir}/decode-*.pl
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_bindir}/sensors.sh
%attr(755,root,root) %{_sbindir}/eeprom*
%attr(755,root,root) %{_sbindir}/i2c*
%attr(755,root,root) %{_sbindir}/sensors-detect
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_sbindir}/isadump
%attr(755,root,root) %{_sbindir}/isaset
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/sensors_modules
%{_mandir}/man8/isadump.8*
%{_mandir}/man8/isaset.8*
%endif
%{_mandir}/man1/sensors.1*
%{_mandir}/man5/sensors.conf.5*
%{_mandir}/man8/i2c*.8*

%files config-default
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sensors.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sysconfig/sensors_modules

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/{developers,kernel}
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/sensors
%{_includedir}/linux/sensors.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsensors.a

%files sensord
%defattr(644,root,root,755)
%attr(754,root,root) %{_sbindir}/sensord
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/sensors
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sysconfig/sensors
%{_mandir}/man8/sensors-detect.8*
%{_mandir}/man8/sensord.8*

%files fancontrol
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/fancontrol
%attr(755,root,root) %{_sbindir}/pwmconfig
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/fancontrol
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sysconfig/fancontrol
%{_mandir}/man8/fancontrol.8*
%{_mandir}/man8/pwmconfig.8*
