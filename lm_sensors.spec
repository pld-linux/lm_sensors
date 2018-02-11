# TODO
# - a big trigger warning how to use fancontrol and to init it first
#
%include	/usr/lib/rpm/macros.perl
Summary:	Hardware health monitoring
Summary(pl.UTF-8):	Monitor stanu sprzętu
Summary(pt_BR.UTF-8):	Ferramentas para monitoração do hardware
Summary(ru.UTF-8):	Утилиты для мониторинга аппаратуры
Summary(uk.UTF-8):	Утиліти для моніторингу апаратури
Name:		lm_sensors
Version:	3.4.0
Release:	3
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.lm-sensors.org/lm-sensors/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	c03675ae9d43d60322110c679416901a
Source1:	sensord.init
Source2:	sensord.sysconfig
Source3:	fancontrol.init
Source4:	fancontrol.sysconfig
Source5:	sensors.sh
Source6:	lm_sensors.init
Source7:	lm_sensors.sysconfig
Source8:	sensord.service
Patch0:		%{name}-ppc.patch
Patch1:		%{name}-iconv-in-libc.patch
Patch2:		%{name}-sensors-detect-PATH.patch
Patch3:		%{name}-make.patch
URL:		http://www.lm-sensors.org/
BuildRequires:	bison
BuildRequires:	flex >= 2.5.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	rrdtool-devel >= 1.2.10
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dev >= 2.9.0-13
Requires:	rc-scripts >= 0.4.2.8
Requires:	systemd-units >= 38
Requires:	uname(release) >= 2.6.5
Obsoletes:	lm_sensors-config-default
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description -l pl.UTF-8
Narzędzie do monitorowania sprzętu w systemach linuksowych
wyposażonych w sprzęt monitorujący, taki jak LM78 lub LM75.

%description -l pt_BR.UTF-8
Ferramentas para monitoração do hardware. Contém uma coleção de
módulos para acesso genérico ao barramento SMBus e monitoração de
hardware.

%description -l ru.UTF-8
Пакет lm_sensors содержит набор модулей для стандартного доступа к
SMBus и мониторинга. ВНИМАНИЕ: для этого необходима специальная
поддержка, отсутствующая в стандартных старых ядрах 2.2.XX!

%description -l uk.UTF-8
Пакет lm_sensors містить набір модулів для стандартного доступу до
SMBus та моніторингу. УВАГА: для цього потрібна спеціальна підтримка,
яка відсутня у стандартних старих ядрах 2.2.XX!

%package libs
Summary:	lm_sensors library
Summary(pl.UTF-8):	Biblioteka lm_sensors
Group:		Libraries
Obsoletes:	liblm_sensors1
Conflicts:	lm_sensors <= 2.9.2-2

%description libs
lm_sensors library.

%description libs -l pl.UTF-8
Biblioteka lm_sensors.

%package devel
Summary:	Header files for lm_sensors
Summary(pl.UTF-8):	Pliki nagłówkowe dla lm_sensors
Summary(pt_BR.UTF-8):	Arquivos necessários ao desenvolvimento de programas que usem o lm_sensors
Summary(ru.UTF-8):	Файлы разработчика для программ, использующих lm_sensors
Summary(uk.UTF-8):	Файли програміста для програм, які використовують lm_sensors
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	liblm_sensors1-devel

%description devel
Header files for lm_sensors.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla lm_sensors.

%description devel -l pt_BR.UTF-8
Arquivos necessários ao desenvolvimento de programas que usem o
lm_sensors.

%description devel -l ru.UTF-8
Пакет lm_sensors-devel включает хедеры и библиотеки, необходимые для
построения программ, использующих данные сенсоров.

%description devel -l uk.UTF-8
Пакет lm_sensors-devel містить хедери та бібліотеки, необхідні для
побудови програм, які використовують дані сенсорів.

%package static
Summary:	Static libraries for lm_sensors
Summary(pl.UTF-8):	Biblioteki statyczne dla lm_sensors
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com lm_sensors
Summary(ru.UTF-8):	Статическая библиотека для программ, использующих lm_sensors
Summary(uk.UTF-8):	Статична бібліотека для програм, які використовують lm_sensors
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for lm_sensors.

%description static -l pl.UTF-8
Biblioteki statyczne dla lm_sensors.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com lm_sensors

%description static -l ru.UTF-8
Пакет lm_sensors-static включает статические библиотеки, необходимые
для построения программ, использующих данные сенсоров.

%description static -l uk.UTF-8
Пакет lm_sensors-static містить статичні бібліотеки, необхідні для
побудови програм, які використовують дані сенсорів.

%package sensord
Summary:	Sensord daemon
Summary(pl.UTF-8):	Demon sensord
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
#Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts
#Requires:	systemd-units >= 38

%description sensord
Sensord daemon.

%description sensord -l pl.UTF-8
Demon sensord.

%package fancontrol
Summary:	Fancontrol daemon
Summary(pl.UTF-8):	Demon sterowania wiatraczkami
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

%description fancontrol -l pl.UTF-8
Demon fancontrol monitoruje obecną temperaturę komputera i ustawia
odpowiednio prędkość wiatraków.

Kluczowym jest, aby poprawnie skonfigurować tego demona (poprzez
uruchomienie service fancontrol init) oraz upewnić się, że progi
temperatury są ustawione poprawnie, by nie spalić wnętrza komputera!

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
	SYSFS_SUPPORT:=1 \
	PROG_EXTRA:="sensord"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{systemdunitdir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} user_install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	ETCDIR=%{_sysconfdir} \
	LIBDIR=%{_libdir} \
	MANDIR=%{_mandir} \
	PROG_EXTRA:="sensord" \
	SYSFS_SUPPORT:=1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/sensord
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/sensord
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/fancontrol
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/fancontrol
install %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/lm_sensors
install %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/lm_sensors
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/sensors.d 

install -p prog/init/lm_sensors.service $RPM_BUILD_ROOT%{systemdunitdir}
install -p %{SOURCE8} $RPM_BUILD_ROOT%{systemdunitdir}/sensord.service

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%pre
if [ -f /var/lock/subsys/sensors_modules ]; then
	mv -f /var/lock/subsys/sensors_modules /var/lock/subsys/lm_sensors
	/sbin/chkconfig --del sensors_modules
fi
if [ -f /etc/sysconfig/sensors_modules ]; then
	. /etc/sysconfig/sensors_modules
	[ -z "$BUS" ] || echo BUS_MODULES=\""$BUS"\" >>/etc/sysconfig/lm_sensors
	[ -z "$CHIP" ] || echo HWMON_MODULES=\""$CHIP"\" >>/etc/sysconfig/lm_sensors
fi

%if 0
#"
%endif

%post
if [ "$1" = 1 ]; then
cat << EOF
 *********************************************************************
 *                                                                   *
 *  NOTE:                                                            *
 *  You have to configure sensors to match your motherboard sensors  *
 *  in /etc/sensors3.conf and /etc/sysconfig/lm_sensors.             *
 *  Use sensors-detect script to find proper modules.                *
 *                                                                   *
 *********************************************************************
EOF
fi
/sbin/chkconfig --add lm_sensors
NORESTART=1
%systemd_post lm_sensors.service

%preun
if [ "$1" = "0" ]; then
	%service lm_sensors stop
	/sbin/chkconfig --del lm_sensors
fi
%systemd_preun lm_sensors.service

%postun
%systemd_reload

%triggerpostun -- %{name} < 3.3.2-2
%systemd_trigger lm_sensors.service

%pre sensord
if [ -f /var/lock/subsys/sensors ]; then
	mv -f /var/lock/subsys/sensors /var/lock/subsys/sensord
fi
if [ -f /etc/rc.d/init.d/sensors ]; then
	/sbin/chkconfig --del sensors
fi
if [ -f /etc/sysconfig/sensors ]; then
	cp -a /etc/sysconfig/sensors /etc/sysconfig/sensord
fi

%post sensord
/sbin/chkconfig --add sensord
%service sensord restart "sensors daemon"
%systemd_post sensord.service

%preun sensord
if [ "$1" = "0" ]; then
	%service sensord stop
	/sbin/chkconfig --del sensord
fi
%systemd_preun sensord.service

%postun sensord
%systemd_reload

%triggerpostun sensord -- %{name}-sensord < 3.3.2-2
%systemd_trigger sensord.service

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
%doc CHANGES CONTRIBUTORS README
%doc doc/{donations,fan-divisors,progs,temperature-sensors,vid}
%doc prog/daemon
%attr(755,root,root) %{_bindir}/sensors-conf-convert
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_bindir}/sensors.sh
%attr(755,root,root) %{_sbindir}/sensors-detect
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_sbindir}/isadump
%attr(755,root,root) %{_sbindir}/isaset
%{_mandir}/man8/isadump.8*
%{_mandir}/man8/isaset.8*
%endif
%{_mandir}/man1/sensors.1*
%{_mandir}/man5/sensors.conf.5*
%{_mandir}/man5/sensors3.conf.5*
%{_mandir}/man8/sensors-conf-convert.8*
%{_mandir}/man8/sensors-detect.8*
%attr(754,root,root) /etc/rc.d/init.d/lm_sensors
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sensors3.conf
%dir %{_sysconfdir}/sensors.d
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/lm_sensors
%{systemdunitdir}/lm_sensors.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsensors.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsensors.so.4

%files devel
%defattr(644,root,root,755)
%doc doc/developers doc/libsensors-API.txt
%attr(755,root,root) %{_libdir}/libsensors.so
%{_includedir}/sensors
%{_mandir}/man3/libsensors.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsensors.a

%files sensord
%defattr(644,root,root,755)
%attr(754,root,root) %{_sbindir}/sensord
%attr(754,root,root) /etc/rc.d/init.d/sensord
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/sensord
%{_mandir}/man8/sensord.8*
%{systemdunitdir}/sensord.service

%files fancontrol
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/fancontrol
%attr(755,root,root) %{_sbindir}/pwmconfig
%attr(754,root,root) /etc/rc.d/init.d/fancontrol
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/fancontrol
%{_mandir}/man8/fancontrol.8*
%{_mandir}/man8/pwmconfig.8*
