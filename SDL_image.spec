Summary:	Simple DirectMedia Layer - Sample Image Loading Library
Summary(pl.UTF-8):	Przykładowa biblioteka do ładowania obrazków
Summary(pt_BR.UTF-8):	Simple DirectMedia Layer - Biblioteca exemplo para carga de Imagens
Name:		SDL_image
Version:	1.2.12
Release:	1
License:	Zlib-like
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz
# Source0-md5:	a0f9098ebe5400f0bdc9b62e60797ecb
Patch0:		%{name}-libpng.patch
URL:		http://www.libsdl.org/projects/SDL_image/
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 8
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libwebp-devel >= 0.1.3
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	SDL >= 1.2.10
Suggests:	libjpeg >= 8
Suggests:	libpng >= 2:1.4.0
Suggests:	libtiff >= 4
Suggests:	libwebp >= 0.1.3
Obsoletes:	libSDL_image1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# NOTE: libraries dlopened by sonames detected at build time:
# libjpeg.so.8
# libpng15.so.15/libpng14.so.14 [note the libpng patch for preferred libs order]
# libtiff.so.5
# libwebp.so.2

%description
This is a simple library to load images of various formats as SDL
surfaces. This library currently supports BMP, GIF, JPEG, LBM, PCX,
PNG, PNM (PBM/PGM/PPM), TGA, TIFF, WebP, XCF and XPM formats.

%description -l pl.UTF-8
Jest to prosta biblioteka służąca do ładowania różnego formatu
obrazków jako powierzchni SDL. W chwili obecnej biblioteka obsługuje
następujące formaty: BMP, GIF, JPEG, LBM, PCX, PNG, PNM (PBM/PGM/PPM),
TGA, TIFF, WebP, XCF oraz XPM.

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-bmp \
	--enable-gif \
	--enable-jpg \
	--enable-jpg-shared \
	--enable-lbm \
	--enable-pcx \
	--enable-png \
	--enable-png-shared \
	--enable-pnm \
	--enable-tga \
	--enable-tif \
	--enable-tif-shared \
	--enable-webp \
	--enable-webp-shared \
	--enable-xcf \
	--enable-xpm \
	--enable-xv

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
%doc CHANGES COPYING README
%attr(755,root,root) %{_bindir}/sdlshow
%attr(755,root,root) %{_libdir}/libSDL_image-1.2.so.*.*.*
%attr(755,root,root) %ghost  %{_libdir}/libSDL_image-1.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_image.so
%{_libdir}/libSDL_image.la
%{_includedir}/SDL/SDL_image.h
%{_pkgconfigdir}/SDL_image.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL_image.a
