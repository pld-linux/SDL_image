Summary:	Simple DirectMedia Layer - Sample Image Loading Library
Name:		SDL_image
Version:	1.1.0
Release:	2
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.devolution.com/~slouken/SDL/projects/SDL_image/src/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel >= 1.1.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is a simple library to load images of various formats as SDL
surfaces. This library currently supports BMP, PPM, PCX, GIF, JPEG,
and PNG formats.

%description -l pl
jest to prosta biblioteka s³u¿±ca do ³adowania ró¿nego formtu obrazków
jako powierzchni SDL. W chwili obecnej biblioteka obs³uguje
nastepuj±ce formaty: BMP, PPM, PCX, GIF, JPEG oraz PNG.

%package devel
Summary:	Header files and more to develop SDL_image applications
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_image applications.

%package static
Summary:	Statis SDL_image libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_image libraries.

%prep
%setup -q 

%build
%configure \
	--enable-bmp \
	--enable-gif \
	--enable-jpg \
	--enable-pcx \
	--enable-png \
	--enable-ppm \
	--enable-tif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/showimage $RPM_BUILD_ROOT%{_bindir}/sdlshow

gzip -9nf README CHANGES

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
