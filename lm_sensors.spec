# TODO
# - unpackaged:
#   /usr/sbin/fancontrol.pl
#
%include	/usr/lib/rpm/macros.perl
Summary:	Hardware health monitoring
Summary(pl):	Monitor stanu sprz�tu
Summary(pt_BR):	Ferramentas para monitora��o do hardware
Summary(ru):	������� ��� ����������� ����������
Summary(uk):	���̦�� ��� ��Φ������� ���������
Name:		lm_sensors
Version:	2.10.0
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://secure.netroedge.com/~lm78/archive/%{name}-%{version}.tar.gz
# Source0-md5:	6a5327c9e291c5e2bef62e2277bce962
Source1:	sensors.init
Source2:	sensors.sysconfig
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
Patch2:		%{name}-iconv-in-libc.patch
Patch3:		%{name}-sensors-detect-PATH.patch
Patch4:		%{name}-CAN-2005-2672.patch
URL:		http://www.lm-sensors.nu/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	bison
BuildRequires:	flex >= 2.5.1
BuildRequires:	perl-modules >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rrdtool-devel >= 1.2.10
BuildRequires:	sysfsutils-devel
Requires:	dev >= 2.9.0-13
Requires:	dmidecode
Obsoletes:	liblm_sensors1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts

%description sensord
Sensord daemon.

%description sensord -l pl
Demon sensord.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
