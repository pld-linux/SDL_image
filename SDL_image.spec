Summary:	Simple DirectMedia Layer - Sample Image Loading Library
Summary(pl):	Przyk³adowa biblioteka do ³adowania obrazków
Summary(pt_BR):	Simple DirectMedia Layer - Biblioteca exemplo para carga de Imagens
Name:		SDL_image
Version:	1.2.2
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz
URL:		http://www.libsdl.org/projects/SDL_image/
Patch0:		%{name}-ac_fixes.patch
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libSDL_image1.2

%define		_prefix		/usr/X11R6

%description
This is a simple library to load images of various formats as SDL
surfaces. This library currently supports BMP, PPM, PCX, GIF, JPEG,
and PNG formats.

%description -l pl
jest to prosta biblioteka s³u¿±ca do ³adowania ró¿nego formtu obrazków
jako powierzchni SDL. W chwili obecnej biblioteka obs³uguje
nastepuj±ce formaty: BMP, PPM, PCX, GIF, JPEG oraz PNG.

%description -l pt_BR
Simple DirectMedia Layer - Biblioteca exemplo para carga de Imagens.

%package devel
Summary:	Header files and more to develop SDL_image applications
Summary(pl):	Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_image
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SDL
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel
Obsoletes:	libSDL_image1.2-devel

%description devel
Header files and more to develop SDL_image applications.

%description devel -l pl
Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_image.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
SDL.

%package static
Summary:	Static SDL_image libraries
Summary(pl):	Statyczne biblioteki SDL_image
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento de aplicações SDL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_image libraries.

%description static -l pl
Statyczne biblioteki SDL_image.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de aplicações SDL.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS" \
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
%doc {README,CHANGES}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
