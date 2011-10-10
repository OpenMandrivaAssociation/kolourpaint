Name: kolourpaint
Summary: kolourpaint
Version: 4.7.41
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPLv2 LGPLv2 GFDL
URL: http://www.kde.org/applications/graphics/kolourpaint/
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: qimageblitz-devel


%description
KolourPaint is a free, easy-to-use paint program for KDE.

%files
%_kde_bindir/kolourpaint
%_kde_datadir/applications/kde4/kolourpaint.desktop
%_kde_appsdir/kolourpaint
%_kde_iconsdir/hicolor/*/apps/kolourpaint.*
%doc COPYING COPYING.LIB COPYING.DOC
%doc %_kde_docdir/HTML/en/kolourpaint/

#-----------------------------------------------------------------------------

%define kolourpaint_lgpl_major 4
%define libkolourpaint_lgpl %mklibname kolourpaint_lgpl %kolourpaint_lgpl_major

%package -n %libkolourpaint_lgpl
Summary: Runtime library for Kolourpaint
Group: System/Libraries

%description -n %libkolourpaint_lgpl
Runtime library for Kolourpaint.

%files -n %libkolourpaint_lgpl
%_kde_libdir/libkolourpaint_lgpl.so.%{kolourpaint_lgpl_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:%{version}
Requires: %libkolourpaint_lgpl = %epoch:%version-%release
Conflicts: kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%_kde_libdir/libkolourpaint_lgpl.so

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

