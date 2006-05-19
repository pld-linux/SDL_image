Summary:	Simple DirectMedia Layer - Sample Image Loading Library
Summary(pl):	Przyk³adowa biblioteka do ³adowania obrazków
Summary(pt_BR):	Simple DirectMedia Layer - Biblioteca exemplo para carga de Imagens
Name:		SDL_image
Version:	1.2.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz
# Source0-md5:	cd006109a73bf7dcc93e1c3ed15ee782
URL:		http://www.libsdl.org/projects/SDL_image/
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	SDL >= 1.2.10
Obsoletes:	libSDL_image1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple library to load images of various formats as SDL
surfaces. This library currently supports BMP, PPM, PCX, GIF, JPEG,
and PNG formats.

%description -l pl
jest to prosta biblioteka s³u¿±ca do ³adowania ró¿nego formatu obrazków
jako powierzchni SDL. W chwili obecnej biblioteka obs³uguje
nastêpuj±ce formaty: BMP, PPM, PCX, GIF, JPEG oraz PNG.

%description -l pt_BR
Simple DirectMedia Layer - Biblioteca exemplo para carga de Imagens.

%package devel
Summary:	Header files and more to develop SDL_image applications
Summary(pl):	Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_image
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SDL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.10
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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Statis SDL_image libraries.

%description static -l pl
Statyczne biblioteki SDL_image.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de aplicações SDL.

%prep
%setup -q

%build
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	jpg_lib=libjpeg.so.62 \
	png_lib=libpng12.so.0 \
	tif_lib=libtiff.so.3 \
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
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install .libs/showimage $RPM_BUILD_ROOT%{_bindir}/sdlshow

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
