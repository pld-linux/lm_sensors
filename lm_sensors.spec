#
# Conditional build:
%bcond_without	dist_kernel	# without kernel for distributions
%bcond_without	smp		# don't build SMP modules
%bcond_without	kernel		# don't build kernel modules
%bcond_without	userspace	# don't build userspace utilities
#
%include	/usr/lib/rpm/macros.perl
Summary:	Hardware health monitoring
Summary(pl):	Monitor stanu sprz�tu
Summary(pt_BR):	Ferramentas para monitora��o do hardware
Summary(ru):	������� ��� ����������� ����������
Summary(uk):	���̦�� ��� ��Φ������� ���������
Name:		lm_sensors
Version:	2.8.3
%define _rel	1
Release:	%{_rel}
License:	GPL
Group:		Applications/System
Source0:	http://secure.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
# Source0-md5:	bb5dff9faa23e414e99383258cd1f532
Source1:	sensors.init
Source2:	sensors.sysconfig
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
URL:		http://www.lm-sensors.nu/
BuildRequires:	bison
BuildRequires:	flex >= 2.5.1
BuildRequires:	perl-modules >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.118
BuildRequires:	rrdtool-devel
%if %{with kernel} && %{with dist_kernel}
BuildRequires:	kernel-i2c-devel >= 2.8.3
BuildRequires:	kernel-headers >= 2.4.0
BuildRequires:	kernel-headers < 2.5.0
%endif
Requires:	dmidecode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	liblm_sensors1

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

%package sensord
Summary:	Sensord daemon
Summary(pl):	Demon sensord
Group:		Daemons
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}

%description sensord
Sensord daemon.

%description sensord -l pl
Demon sensord.

%package devel
Summary:	Header files for lm_sensors
Summary(pl):	Pliki nag��wkowe dla lm_sensors
Summary(pt_BR):	Arquivos necess�rios ao desenvolvimento de programas que usem o lm_sensors
Summary(ru):	����� ������������ ��� ��������, ������������ lm_sensors
Summary(uk):	����� ������ͦ��� ��� �������, �˦ �������������� lm_sensors
Group:		Development/Libraries
Requires:	%{name} = %{version}
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
Requires:	%{name}-devel = %{version}

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

%package -n kernel-i2c-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl):	Modu�y j�dra dla r�nego rodzaju sensor�w
Group:		Applications/System
Release:	%{_rel}@%{_kernel_ver_str}
Requires(post,postun):	/sbin/depmod
%{?with_dist_kernel:%requires_releq_kernel_up}
%{?with_dist_kernel:Requires:	kernel-i2c >= 2.8.2}
Provides:	%{name}-modules = %{version}
Obsoletes:	%{name}-modules
Obsoletes:	kernel-misc-lm_sensors

%description -n kernel-i2c-%{name}
Kernel modules for various buses and monitor chips.

%description -n kernel-i2c-%{name} -l pl
Modu�y j�dra dla r�nego rodzaju sensor�w monitoruj�cych.

%package -n kernel-smp-i2c-%{name}
Summary:	Kernel modules for various buses and monitor chips
Summary(pl):	Modu�y j�dra dla r�nego rodzaju sensor�w
Group:		Applications/System
Release:	%{_rel}@%{_kernel_ver_str}
Requires(post,postun):	/sbin/depmod
%{?with_dist_kernel:%requires_releq_kernel_smp}
%{?with_dist_kernel:Requires:	kernel-smp-i2c >= 2.8.2}
Provides:	%{name}-modules = %{version}
Obsoletes:	%{name}-modules
Obsoletes:	kernel-smp-misc-lm_sensors

%description -n kernel-smp-i2c-%{name}
Kernel SMP modules for various buses and monitor chips.

%description -n kernel-smp-i2c-%{name} -l pl
Modu�y j�dra SMP dla r�nego rodzaju sensor�w monitoruj�cych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%if %{with kernel} && %{with smp}
# SMP
%{__make} all-kernel-busses all-kernel-chips \
	CC="%{kgcc}" \
	OPTS="%{rpmcflags} -D__KERNEL_SMP=1" \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=1

%{__make} install-kernel-busses install-kernel-chips \
	MODPREF=kernel-smp-modules \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=1

%{__make} clean
%endif

%if %{with kernel}
# UP
%{__make} all-kernel-busses all-kernel-chips \
	CC="%{kgcc}" \
	OPTS="%{rpmcflags}" \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=%{_kernelsrcdir}/include \
	SMP=0
%endif

%if %{with userspace}
%{__make} user \
	CC="%{__cc}" \
	OPTS="%{rpmcflags}" \
	LINUX=/dev/null \
	LINUX_HEADERS=%{_kernelsrcdir}/include \
	I2C_HEADERS=/usr/include \
	PROG_EXTRA:="sensord dump"

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
	LINUX=/dev/null \
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
	MANDIR=%{_mandir} \
	PROG_EXTRA:="sensord dump" \
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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

%post	-n kernel-i2c-%{name}
%depmod %{_kernel_ver}

%postun -n kernel-i2c-%{name}
%depmod %{_kernel_ver}

%post	-n kernel-smp-i2c-%{name}
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-i2c-%{name}
%depmod %{_kernel_ver}smp

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc BACKGROUND BUGS CHANGES README README.thinkpad TODO doc/{busses,chips}
%doc doc/{FAQ,donations,fan-divisors,progs,temperature-sensors,*html,vid}
%doc prog/{config,daemon,eepromer/README*,matorb,maxilife}
%attr(755,root,root) %{_bindir}/decode-*.pl
%attr(755,root,root) %{_bindir}/sensors
%attr(755,root,root) %{_sbindir}/sensors-detect
%attr(755,root,root) %{_sbindir}/eeprom*
%attr(755,root,root) %{_sbindir}/fancontrol
%attr(755,root,root) %{_sbindir}/i2c*
%attr(755,root,root) %{_sbindir}/isadump
%attr(755,root,root) %{_sbindir}/pwmconfig
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
%{_includedir}/linux/sensors.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsensors.a
%endif

%if %{with kernel}
%files -n kernel-i2c-%{name}
%defattr(644,root,root,755)
%dir /lib/modules/%{_kernel_ver}/kernel/drivers/i2c/busses
/lib/modules/%{_kernel_ver}/kernel/drivers/i2c/busses/*.o*
%dir /lib/modules/%{_kernel_ver}/kernel/drivers/i2c/chips
/lib/modules/%{_kernel_ver}/kernel/drivers/i2c/chips/*.o*

%if %{with smp}
%files -n kernel-smp-i2c-%{name}
%defattr(644,root,root,755)
%dir /lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/busses
/lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/busses/*.o*
%dir /lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/chips
/lib/modules/%{_kernel_ver}smp/kernel/drivers/i2c/chips/*.o*
%endif
%endif
