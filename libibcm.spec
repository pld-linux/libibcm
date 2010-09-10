Summary:	Userspace InfiniBand Connection Manager
Summary(pl.UTF-8):	Zarządca połączeń InfiniBand w przestrzeni użytkownika
Name:		libibcm
Version:	1.0.5
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
# Source0-md5:	7ede8d7e96d6a65f09f289767bd931ea
URL:		http://www.openfabrics.org/
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libibcm provides a userspace InfiniBand Communication Managment
library.

%description -l pl.UTF-8
libibcm to biblioteka zarządzająca połączeniami InfiniBand (InfiniBand
Communication Management) w przestrzeni użytkownika.

%package devel
Summary:	Header files for libibcm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libibcm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libibverbs-devel

%description devel
Header files for libibcm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libibcm.

%package static
Summary:	Static libibcm library
Summary(pl.UTF-8):	Statyczna biblioteka libibcm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libibcm library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę libibcm.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libibcm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibcm.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibcm.so
%{_libdir}/libibcm.la
%{_includedir}/infiniband/cm.h
%{_includedir}/infiniband/cm_abi.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libibcm.a
