Summary:	Simple DirectMedia Layer - Sample Image Loading Library
Name:		SDL_image
Version:	1.0.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.devolution.com/~slouken/SDL/projects/SDL_image/src/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel >= 1.0.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
This is a simple library to load images of various formats as SDL surfaces.
This library currently supports BMP, PPM, PCX, GIF, JPEG, and PNG formats.

%package devel
Summary:	Header files and more to develop SDL_image applications
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_image applications.

%package static
Summary:	Statis SDL_image libraries
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Requires:	SDL-devel

%description static
Statis SDL_image libraries.

%prep
%setup -q 

%build
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/showimage
%attr(755,root,roo) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,roo) %{_libdir}/lib*.so
%{_includedir}/SDL/*

%files static
%attr(644,root,roo) %{_libdir}/lib*.a
