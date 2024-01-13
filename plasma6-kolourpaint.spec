%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A free, easy-to-use paint program for KDE
Name:		plasma6-kolourpaint
Version:	24.01.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/graphics/kolourpaint/
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kolourpaint-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KSaneCore6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(F6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6JobWidgets)

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
