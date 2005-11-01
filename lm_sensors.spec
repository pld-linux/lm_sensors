# TODO
# - unpackaged:
#   /usr/sbin/fancontrol.pl
#
# Conditional build:
%bcond_without	dist_kernel	# without kernel for distributions
%bcond_without	smp		# don't build SMP modules
%bcond_without	kernel		# build kernel 2.4 modules
%bcond_without	userspace	# don't build userspace utilities

%ifarch %{x8664}
%undefine with_kernel
%endif

%include	/usr/lib/rpm/macros.perl
Summary:	Hardware health monitoring
Summary(pl):	Monitor stanu sprz�tu
Summary(pt_BR):	Ferramentas para monitora��o do hardware
Summary(ru):	������� ��� ����������� ����������
Summary(uk):	���̦�� ��� ��Φ������� ���������
Name:		lm_sensors
Version:	2.9.2
%define _rel	2.1
Release:	%{_rel}
License:	GPL
Group:		Applications/System
Source0:	http://secure.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
# Source0-md5:	229f83cfbd081d5e7bd46885efec1c72
Source1:	sensors.init
Source2:	sensors.sysconfig
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
Patch2:		%{name}-iconv-in-libc.patch
Patch3:		%{name}-sensors-detect-PATH.patch
Patch4:		%{name}-CAN-2005-2672.patch
URL:		http://www.lm-sensors.nu/
BuildRequires:	rpmbuild(macros) >= 1.213
%if %{with userspace}
BuildRequires:	bison
BuildRequires:	flex >= 2.5.1
BuildRequires:	perl-modules >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rrdtool-devel >= 1.2.10
%endif
%if %{with kernel} && %{with dist_kernel}
BuildRequires:	kernel24-i2c-devel >= 2.9.0
BuildRequires:	kernel24-headers >= 2.4.0
BuildRequires:	kernel24-headers < 2.5.0
%endif
Requires:	dev >= 2.9.0-13
Requires:	dmidecode
Obsoletes:	liblm_sensors1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_kernelsrcdir		/usr/src/linux-2.4

%description
Tools for monitoring the hardware health of Linux systems containing
hardware health monitoring hardware such as the LM78 and LM75.

%description -l pl
Narz�dzie do monitorowania sprz�tu w systemach linuksowych
wyposa�onych w sprz�t monitoruj�cy, taki jak LM78 lub LM75.

%description -l pt_BR
Ferramentas para monitora��o do hardware. Cont�m uma cole��o de
m�dulos para acesso gen�rico ao barramento SMBus e monitora��o de
hardware.

%description -l ru
����� lm_sensors �������� ����� ������� ��� ������������ ������� �
SMBus � �����������. ��������: ��� ����� ���������� �����������
���������, ������������� � ����������� ������ ����� 2.2.XX!

%description -l uk
����� lm_sensors ͦ����� ��¦� ����̦� ��� ������������ ������� ��
SMBus �� ��Φ�������. �����: ��� ����� ���Ҧ��� ���æ����� Ц�������,
��� צ������ � ����������� ������ ����� 2.2.XX!

%package libs
Summary:	lm_sensors library
Summary(pl):	Biblioteka lm_sensors
Group:		Libraries

%description libs
lm_sensors library.

%description libs -l pl
Biblioteka lm_sensors.

%package devel
Summary:	Header files for lm_sensors
Summary(pl):	Pliki nag��wkowe dla lm_sensors
Summary(pt_BR):	Arquivos necess�rios ao desenvolvimento de programas que usem o lm_sensors
Summary(ru):	����� ������������ ��� ��������, ������������ lm_sensors
Summary(uk):	����� ������ͦ��� ��� �������, �˦ �������������� lm_sensors
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	liblm_sensors1-devel

%description devel
Header files for lm_sensors.

%description devel -l pl
Pliki nag��wkowe dla lm_sensors.

%description devel -l pt_BR
Arquivos necess�rios ao desenvolvimento de programas que usem o
lm_sensors.

%description devel -l ru
����� lm_sensors-devel �������� ������ � ����������, ����������� ���
���������� ��������, ������������ ������ ��������.

%description devel -l uk
����� lm_sensors-devel ͦ����� ������ �� ¦�̦�����, ����Ȧ�Φ ���
�������� �������, �˦ �������������� ��Φ �����Ҧ�.

%package static
Summary:	Static libraries for lm_sensors
Summary(pl):	Biblioteki statyczne dla lm_sensors
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com lm_sensors
Summary(ru):	����������� ���������� ��� ��������, ������������ lm_sensors
Summary(uk):	�������� ¦�̦����� ��� �������, �˦ �������������� lm_sensors
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for lm_sensors.

%description static -l pl
Biblioteki statyczne dla lm_sensors.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com lm_sensors

%description static -l ru
����� lm_sensors-static �������� ����������� ����������, �����������
��� ���������� ��������, ������������ ������ ��������.

%description static -l uk
����� lm_sensors-static ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ���
�������� �������, �˦ �������������� ��Φ �����Ҧ�.

%package sensord
Summary:	Sensord daemon
Summary(pl):	Demon sensord
Group:		Daemons
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description sensord
Sensord daemon.

%description sensord -l pl
Demon sensord.

%package -n kernel24-i2c-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl):	Modu�y j�dra dla r�nego rodzaju sensor�w
Group:		Applications/System
Release:	%{_rel}@%{_kernel_ver_str}
Requires(post,postun):	/sbin/depmod
%{?with_dist_kernel:%requires_releq_kernel_up}
%{?with_dist_kernel:Requires:	i2c >= 2.9.0}
Provides:	%{name}-modules = %{version}-%{release}
Obsoletes:	kernel-misc-lm_sensors

%description -n kernel24-i2c-%{name}
Kernel modules for various buses and monitor chips.

%description -n kernel24-i2c-%{name} -l pl
Modu�y j�dra dla r�nego rodzaju sensor�w monitoruj�cych.

%package -n kernel24-smp-i2c-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl):	Modu�y j�dra dla r�nego rodzaju sensor�w
Group:		Applications/System
Release:	%{_rel}@%{_kernel_ver_str}
Requires(post,postun):	/sbin/depmod
%{?with_dist_kernel:%requires_releq_kernel_smp}
%{?with_dist_kernel:Requires:	i2c >= 2.9.0}
Provides:	%{name}-modules = %{version}-%{release}
Obsoletes:	kernel-smp-misc-lm_sensors

%description -n kernel24-smp-i2c-%{name}
Kernel SMP modules for various buses and monitor chips.

%description -n kernel24-smp-i2c-%{name} -l pl
Modu�y j�dra SMP dla r�nego rodzaju sensor�w monitoruj�cych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
	PROG_EXTRA:="sensord"

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
/sbin/chkconfig --add sensors
if [ -f /var/lock/subsys/sensors ]; then
	/etc/rc.d/init.d/sensors restart >&2
else
	echo "You have to configure sensors modules in /etc/sysconfig/sensors"
	echo
	echo "Run \"/etc/rc.d/init.d/sensors start\" to start sensors daemon." >&2
fi

%preun sensord
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/sensors ]; then
		/etc/rc.d/init.d/sensors stop >&2
	fi
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
