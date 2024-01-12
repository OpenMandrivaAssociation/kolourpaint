%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A free, easy-to-use paint program for KDE
Name:		plasma6-kolourpaint
Version:	24.01.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/kolourpaint/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kolourpaint-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KSaneCore6)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)

%description
KolourPaint is a free, easy-to-use paint program for KDE.

%files -f kolourpaint.lang
%{_datadir}/applications/org.kde.kolourpaint.desktop
%{_datadir}/kolourpaint
%{_datadir}/metainfo/org.kde.kolourpaint.appdata.xml
%{_bindir}/kolourpaint
%{_iconsdir}/hicolor/*/apps/kolourpaint.*
%{_libdir}/libkolourpaint_lgpl.so*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kolourpaint-%{?git:master}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kolourpaint --with-html
