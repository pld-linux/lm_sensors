# TODO
# - unpackaged:
#   /usr/sbin/fancontrol.pl
#
# Conditional build:
%bcond_without	dist_kernel	# without kernel for distributions
%bcond_without	smp		# don't build SMP modules
%bcond_without	kernel		# build kernel 2.4 modules
				# (NOTE: KERNEL 2.6 MODULES ARE NOT BUILT FROM FROM THIS SPEC)
%bcond_without	userspace	# don't build userspace utilities

%ifarch %{x8664}
%undefine with_kernel
%endif

%define _rel	1
%include	/usr/lib/rpm/macros.perl
Summary:	Hardware health monitoring
Summary(pl.UTF-8):	Monitor stanu sprzętu
Summary(pt_BR.UTF-8):	Ferramentas para monitoração do hardware
Summary(ru.UTF-8):	Утилиты для мониторинга аппаратуры
Summary(uk.UTF-8):	Утиліти для моніторингу апаратури
Name:		lm_sensors
Version:	2.10.5
Release:	%{_rel}
License:	GPL
Group:		Applications/System
Source0:	http://dl.lm-sensors.org/lm-sensors/releases/%{name}-%{version}.tar.gz
# Source0-md5:	77f96bc8a7773e95b2990d756e4925d6
Source1:	sensors.init
Source2:	sensors.sysconfig
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
Patch2:		%{name}-iconv-in-libc.patch
Patch3:		%{name}-sensors-detect-PATH.patch
URL:		http://www.lm-sensors.org/
BuildRequires:	rpmbuild(macros) >= 1.268
%if %{with userspace}
BuildRequires:	bison
BuildRequires:	flex >= 2.5.1
BuildRequires:	perl-modules >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rrdtool-devel >= 1.2.10
BuildRequires:	sysfsutils-devel
%endif
%if %{with kernel} && %{with dist_kernel}
BuildRequires:	kernel24-headers < 2.5.0
BuildRequires:	kernel24-headers >= 2.4.0
BuildRequires:	kernel24-i2c-devel >= 2.9.0
%endif
Requires:	dev >= 2.9.0-13
Requires:	dmidecode
Obsoletes:	liblm_sensors1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_kernelsrcdir		/usr/src/linux-2.4

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
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts

%description sensord
Sensord daemon.

%description sensord -l pl.UTF-8
Demon sensord.

%package -n kernel24-i2c-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl.UTF-8):	Moduły jądra dla różnego rodzaju sensorów
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Applications/System
Requires(post,postun):	/sbin/depmod
%{?with_dist_kernel:%requires_releq_kernel_up}
%{?with_dist_kernel:Requires:	i2c >= 2.9.0}
Provides:	%{name}-modules = %{version}-%{release}
Obsoletes:	kernel-misc-lm_sensors

%description -n kernel24-i2c-%{name}
Kernel modules for various buses and monitor chips.

%description -n kernel24-i2c-%{name} -l pl.UTF-8
Moduły jądra dla różnego rodzaju sensorów monitorujących.

%package -n kernel24-smp-i2c-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl.UTF-8):	Moduły jądra dla różnego rodzaju sensorów
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Applications/System
Requires(post,postun):	/sbin/depmod
%{?with_dist_kernel:%requires_releq_kernel_smp}
%{?with_dist_kernel:Requires:	i2c >= 2.9.0}
Provides:	%{name}-modules = %{version}-%{release}
Obsoletes:	kernel-smp-misc-lm_sensors

%description -n kernel24-smp-i2c-%{name}
Kernel SMP modules for various buses and monitor chips.

%description -n kernel24-smp-i2c-%{name} -l pl.UTF-8
Moduły jądra SMP dla różnego rodzaju sensorów monitorujących.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%if %{with kernel}
# workaround to avoid unresolved dmi* symbols in i2c-piix4.o
install -d fakelinux
:> fakelinux/.config
%ifarch %{ix86}
echo 'CONFIG_X86=y' >> fakelinux/.config
%endif
%ifarch %{ix86} %{x8664} alpha ppc
echo 'CONFIG_IPMI_HANDLER=m' >> fakelinux/.config
%endif

%if %{with smp}
# SMP
%{__make} all-kernel-busses all-kernel-chips \
	CC="%{kgcc}" \
	OPTS="%{rpmcflags} -D__KERNEL_SMP=1" \
	LINUX=`pwd`/fakelinux \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=1

%{__make} install-kernel-busses install-kernel-chips \
	MODPREF=kernel-smp-modules \
	LINUX=`pwd`/fakelinux \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=1

%{__make} clean
%endif

# UP
%{__make} all-kernel-busses all-kernel-chips \
	CC="%{kgcc}" \
	OPTS="%{rpmcflags}" \
	LINUX=`pwd`/fakelinux \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=0
%endif

%if %{with userspace}
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
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with kernel}
%{__make} install-kernel-busses install-kernel-chips \
	DESTDIR=$RPM_BUILD_ROOT \
	MODPREF=/lib/modules/%{_kernel_ver} \
	LINUX=`pwd`/fakelinux \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=0
%endif

%if %{with userspace}
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

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

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/sensors
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/sensors

# i2c API for userspace - included in glibc-kernel-headers
rm -f $RPM_BUILD_ROOT%{_includedir}/linux/i2c-dev.h
%endif

%if %{with kernel} && %{with smp}
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/{busses,chips}
install kernel-smp-modules/kernel/drivers/i2c/busses/*.o \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/busses
install kernel-smp-modules/kernel/drivers/i2c/chips/*.o \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/chips
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post sensord
if [ "$1" = 1 ]; then
	echo "You have to configure sensors modules in /etc/sysconfig/sensors"
fi
/sbin/chkconfig --add sensors
%service sensors restart "sensors daemon"

%preun sensord
if [ "$1" = "0" ]; then
	%service sensors stop
	/sbin/chkconfig --del sensors
fi

%post	-n kernel24-i2c-%{name}
%depmod %{_kernel_ver}

%postun -n kernel24-i2c-%{name}
%depmod %{_kernel_ver}

%post	-n kernel24-smp-i2c-%{name}
%depmod %{_kernel_ver}smp

%postun -n kernel24-smp-i2c-%{name}
%depmod %{_kernel_ver}smp

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc BACKGROUND BUGS CHANGES README README.thinkpad TODO doc/{busses,chips}
%doc doc/{FAQ,donations,fan-divisors,progs,temperature-sensors,*html,vid}
%doc prog/{config,daemon,eepromer/README*,matorb,maxilife}
%attr(755,root,root) %{_bindir}/ddcmon
%attr(755,root,root) %{_bindir}/decode-*.pl
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_sbindir}/sensors-detect
%attr(755,root,root) %{_sbindir}/eeprom*
%attr(755,root,root) %{_sbindir}/fancontrol
%attr(755,root,root) %{_sbindir}/i2c*
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_sbindir}/isadump
%attr(755,root,root) %{_sbindir}/isaset
%{_mandir}/man8/isadump.8*
%{_mandir}/man8/isaset.8*
%endif
%attr(755,root,root) %{_sbindir}/pwmconfig
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sensors.conf
%{_mandir}/man1/sensors.1*
%{_mandir}/man5/sensors.conf.5*
%{_mandir}/man8/fancontrol.8*
%{_mandir}/man8/i2c*.8*
%{_mandir}/man8/pwmconfig.8*
%{_mandir}/man8/sensors-detect.8*

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
%attr(754,root,root) /etc/rc.d/init.d/sensors
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/sensors
%{_mandir}/man8/sensord.8*
%endif

%if %{with kernel}
%files -n kernel24-i2c-%{name}
%defattr(644,root,root,755)
%dir /lib/modules/%{_kernel_ver}/kernel/drivers/i2c/busses
/lib/modules/%{_kernel_ver}/kernel/drivers/i2c/busses/*.o*
%dir /lib/modules/%{_kernel_ver}/kernel/drivers/i2c/chips
/lib/modules/%{_kernel_ver}/kernel/drivers/i2c/chips/*.o*

%if %{with smp}
%files -n kernel24-smp-i2c-%{name}
%defattr(644,root,root,755)
%dir /lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/busses
/lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/busses/*.o*
%dir /lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/chips
/lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/chips/*.o*
%endif
%endif
