%define name SDL_image
%define version 1.0.4
%define release 1

Summary: Simple DirectMedia Layer - Sample Image Loading Library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Copyright: LGPL
Group: System Environment/Libraries
BuildRoot: /var/tmp/%{name}-buildroot
Prefix: %{_prefix}
Packager: Hakan Tandogan <hakan@iconsult.com>
BuildRequires: SDL-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
#BuildRequires: libtiff-devel

%description
This is a simple library to load images of various formats as SDL surfaces.
This library currently supports BMP, PPM, PCX, GIF, JPEG, and PNG formats.

%package devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/Libraries
Requires: %{name}
Requires: SDL-devel

%description devel
This is a simple library to load images of various formats as SDL surfaces.
This library currently supports BMP, PPM, PCX, GIF, JPEG, and PNG formats.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup 

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{prefix}/bin/showimage
%{prefix}/lib/lib*.so.*
%{prefix}/lib/lib*.so

%files devel
%defattr(-,root,root)
%{prefix}/lib/*a
%{prefix}/include/SDL/

%changelog
* Wed Jan 19 2000 Sam Lantinga 
- converted to get package information from configure
* Tue Jan 18 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file
