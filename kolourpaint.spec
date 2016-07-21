Summary:	A free, easy-to-use paint program for KDE
Name:		kolourpaint
Version:	16.04.3
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/kolourpaint/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0

%description
KolourPaint is a free, easy-to-use paint program for KDE.

%files
%doc COPYING COPYING.LIB COPYING.DOC
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
Requires:	kdelibs-devel
Conflicts:	kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_libdir}/libkolourpaint_lgpl.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
