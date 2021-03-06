Name: cbgp
Summary: BGP routing solver (C-BGP)
Packager: Bruno Quoitin (bruno.quoitin@uclouvain.be)
%define version 2.2.0
Version: %{version}
%define release 1%{?dist}
Release: %{release}
License: GPL/LGPL
Vendor: The C-BGP Team
Url: http://cbgp.info.ucl.ac.be
Source0: %{name}-%{version}.tar.gz
Group: Applications/Engineering
%define mybuidroot /var/tmp/%{name}-build
BuildRoot: %{mybuildroot}
Requires: libgds >= 2.2.0 pcre readline zlib pkgconfig
BuildRequires: libgds-devel >= 2.2.0 zlib-devel readline-devel >= 4 pcre-devel >= 4
#ExclusiveArch: i386

%description
C-BGP is an efficient solver for BGP, the de facto standard protocol used for exchanging routing information accross domains in the Internet. C-BGP is aimed at computing the outcome of the BGP decision process in networks composed of several routers. For this purpose, it takes into account the routers' configuration, the externally received BGP routes and the network topology. It supports the complete BGP decision process, versatile import and export filters, route-reflection, and experimental attributes such as redistribution communities. It is easily configurable through a CISCO-like command-line interface.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS"
PKG_CONFIG_PATH="$PKG_CONFIG_PATH:%{_libdir}/pkgconfig" \
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--mandir=%{_mandir} \
	--localstatedir=%{_localstatedir} \
	--libdir=%{_libdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--sysconfdir=%{_sysconfdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} bindir=$RPM_BUILD_ROOT%{_bindir} \
    mandir=$RPM_BUILD_ROOT%{_mandir} libdir=$RPM_BUILD_ROOT%{_libdir} \
    localstatedir=$RPM_BUILD_ROOT%{_localstatedir} \
    datadir=$RPM_BUILD_ROOT%{_datadir} \
    includedir=$RPM_BUILD_ROOT%{_includedir} \
    sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} install
make check

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_prefix}/lib
%{_prefix}/bin
%{_prefix}/include/cbgp

