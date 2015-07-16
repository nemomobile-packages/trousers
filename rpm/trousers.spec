Name: trousers
Version: 0.3.13
Release: 1
Summary: Middleware to access TPM
URL: http://trousers.sourceforge.net/
Group: System/Base
License: BSD
Source0: %{name}-%{version}.tar.gz
BuildRequires: automake > 1.4, autoconf > 1.4
BuildRequires: pkgconfig, libtool
BuildRequires: pkgconfig(openssl)


%description
%{summary}.

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/tcsd.conf
%{_libdir}/*.so.*
%{_sbindir}/tcsd


%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a
%{_libdir}/*.so
%dir %{_includedir}/tss
%dir %{_includedir}/trousers
%{_includedir}/tss/*.h
%{_includedir}/trousers/*.h


%package devel-doc
Summary: Development documentation for %{name}
Group: Documentation

%description devel-doc
%{summary}.

%files devel-doc
%defattr(-,root,root,-)
%{_mandir}/man3/*


%package doc
Summary: Documentation for %{name}
Group: Documentation

%description doc
%{summary}.

%files doc
%defattr(-,root,root,-)
%{_mandir}/man5/*
%{_mandir}/man8/*


%prep
%setup -q -n %{name}-%{version}/%{name}


%build
autoreconf -vfi
%configure
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
