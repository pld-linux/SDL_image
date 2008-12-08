Summary:	Simple DirectMedia Layer - Sample Image Loading Library
Summary(pl.UTF-8):	Przykładowa biblioteka do ładowania obrazków
Summary(pt_BR.UTF-8):	Simple DirectMedia Layer - Biblioteca exemplo para carga de Imagens
Name:		SDL_image
Version:	1.2.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz
# Source0-md5:	a729ff61f74f0a45ec7fe36354cf938e
URL:		http://www.libsdl.org/projects/SDL_image/
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 2:1.2.0
BuildRequires:	libtiff-devel >= 3
BuildRequires:	libtool
Requires:	SDL >= 1.2.10
Obsoletes:	libSDL_image1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple library to load images of various formats as SDL
surfaces. This library currently supports BMP, PPM, PCX, GIF, JPEG,
and PNG formats.

%description -l pl.UTF-8
jest to prosta biblioteka służąca do ładowania różnego formatu obrazków
jako powierzchni SDL. W chwili obecnej biblioteka obsługuje
następujące formaty: BMP, PPM, PCX, GIF, JPEG oraz PNG.

%description -l pt_BR.UTF-8
Simple DirectMedia Layer - Biblioteca exemplo para carga de Imagens.

%package devel
Summary:	Header files and more to develop SDL_image applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL_image
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SDL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.10
Obsoletes:	libSDL_image1.2-devel

%description devel
Header files and more to develop SDL_image applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL_image.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
SDL.

%package static
Summary:	Static SDL_image libraries
Summary(pl.UTF-8):	Statyczne biblioteki SDL_image
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento de aplicações SDL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Statis SDL_image libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SDL_image.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de aplicações SDL.

%prep
%setup -q

rm -f acinclude.m4

%build
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
%attr(755,root,root) %{_bindir}/sdlshow
%attr(755,root,root) %{_libdir}/libSDL_image-*.so.*.*.*
%attr(755,root,root) %ghost  %{_libdir}/libSDL_image-1.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_image.so
%{_libdir}/libSDL_image.la
%{_includedir}/SDL/SDL_image.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL_image.a
