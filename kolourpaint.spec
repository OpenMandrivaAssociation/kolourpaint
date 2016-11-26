Summary:	A free, easy-to-use paint program for KDE
Name:		kolourpaint
Version:	16.08.3
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/kolourpaint/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KDELibs4Support)
BuildRequires:	cmake(KF5Sane)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
KolourPaint is a free, easy-to-use paint program for KDE.

%files
%doc %{_kde_docdir}/HTML/en/kolourpaint/
%{_kde_applicationsdir}/kolourpaint.desktop
%{_kde_appsdir}/kolourpaint
%{_datadir}/appdata/kolourpaint.appdata.xml
%{_kde_bindir}/kolourpaint
%{_kde_iconsdir}/hicolor/*/apps/kolourpaint.*

#----------------------------------------------------------------------------

%define kolourpaint_lgpl_major 4
%define libkolourpaint_lgpl %mklibname kolourpaint_lgpl %{kolourpaint_lgpl_major}

%package -n %{libkolourpaint_lgpl}
Summary:	Runtime library for Kolourpaint
Group:		System/Libraries

%description -n %{libkolourpaint_lgpl}
Runtime library for Kolourpaint.

%files -n %{libkolourpaint_lgpl}
%{_kde_libdir}/libkolourpaint_lgpl.so.%{kolourpaint_lgpl_major}*

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
%{_kde_libdir}/libkolourpaint_lgpl.so

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
