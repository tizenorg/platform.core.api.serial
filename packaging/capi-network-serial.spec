Name:       capi-network-serial
Summary:    Network Serial Framework
Version: 0.0.7
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(capi-base-common)

BuildRequires:  cmake


%description
Network Serial Framework

%package devel
Summary:    Network Serial Framework (DEV)
Group:      TO_BE/FILLED
Requires:   %{name} = %{version}-%{release}

%description devel
Network Serial Framework (DEV).

%prep
%setup -q

%build
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`
cmake . -DCMAKE_INSTALL_PREFIX=/usr -DFULLVER=%{version} -DMAJORVER=${MAJORVER}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest capi-network-serial.manifest
%defattr(-,root,root,-)
%{_libdir}/libcapi-network-serial.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/network/serial.h
%{_libdir}/pkgconfig/capi-network-serial.pc
%{_libdir}/libcapi-network-serial.so

