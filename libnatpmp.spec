%define major 1
%define libname %mklibname natpmp %{major}
%define develname %mklibname -d natpmp

Summary: Direct concurrent to the UPnP IGD specification
Name: libnatpmp
Version: 20230423
Release: 2
License: LGPLv2+
Group: System/Libraries
URL: https://miniupnp.free.fr/
Source: http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz

%description
libnatpmp is an attempt to make a portable and fully compliant
implementation of the protocol for the client side. It is based on non
blocking sockets and all calls of the API are asynchronous. It is
therefore very easy to integrate the NAT-PMP code to any event driven code.

%package -n %{libname}
Summary: Direct concurrent to the UPnP IGD specification
Group: System/Libraries

%description -n %{libname}
libnatpmp is an attempt to make a portable and fully compliant
implementation of the protocol for the client side. It is based on non
blocking sockets and all calls of the API are asynchronous. It is
therefore very easy to integrate the NAT-PMP code to any event driven code.

%package -n %{develname}
Summary: Header files, libraries and development documentation for libnatpmp
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname} 
This package contains the header files and development documentation for
libnatpmp. If you like to develop programs using miniupnpc, you will need
to install libnatpmp-devel.

%prep
%autosetup -p1

%build
%make_build \
	LDFLAGS="%ldflags" \
	CFLAGS="-fPIC -Wall -DENABLE_STRNATPMPERR %{optflags}" \
	EXTRA_LD="%{?__global_ldflags}"

%install
%__make install \
	INSTALLPREFIX=%{buildroot}%{_prefix} \
	INSTALLDIRLIB=%{buildroot}%{_libdir} \
	INSTALLDIRINC="%{buildroot}%{_includedir}" \
	INSTALLDIRBIN="%{buildroot}%{_bindir}"

# Make install seems to forget this
cp natpmp_declspec.h %{buildroot}%{_includedir}/

rm -f %{buildroot}%{_libdir}/*.a

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*.h
