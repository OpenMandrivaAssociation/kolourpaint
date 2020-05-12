%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A free, easy-to-use paint program for KDE
Name:		kolourpaint
Version:	20.04.1
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/kolourpaint/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Sane)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
KolourPaint is a free, easy-to-use paint program for KDE.

%files -f %{name}.lang
%{_datadir}/applications/org.kde.kolourpaint.desktop
%{_datadir}/kolourpaint
%{_datadir}/metainfo/org.kde.kolourpaint.appdata.xml
%{_datadir}/kxmlgui5/kolourpaint
%{_bindir}/kolourpaint
%{_iconsdir}/hicolor/*/apps/kolourpaint.*

#----------------------------------------------------------------------------

%define kolourpaint_lgpl_major 5
%define libkolourpaint_lgpl %mklibname kolourpaint_lgpl %{kolourpaint_lgpl_major}

%package -n %{libkolourpaint_lgpl}
Summary:	Runtime library for Kolourpaint
Group:		System/Libraries
Obsoletes:	%{mklibname kolourpaint_lgpl 4} < 2:16.08.3

%description -n %{libkolourpaint_lgpl}
Runtime library for Kolourpaint.

%files -n %{libkolourpaint_lgpl}
%{_libdir}/libkolourpaint_lgpl.so.%{kolourpaint_lgpl_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkolourpaint_lgpl} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_libdir}/libkolourpaint_lgpl.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
