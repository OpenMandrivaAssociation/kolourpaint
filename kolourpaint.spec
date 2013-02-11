Name:		kolourpaint
Summary:	A free, easy-to-use paint program for KDE
Version:	4.10.0
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
URL:		http://www.kde.org/applications/graphics/kolourpaint/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(qimageblitz)

%description
KolourPaint is a free, easy-to-use paint program for KDE.

%files
%doc COPYING COPYING.LIB COPYING.DOC
%doc %{_kde_docdir}/HTML/en/kolourpaint/
%{_kde_bindir}/kolourpaint
%{_kde_applicationsdir}/kolourpaint.desktop
%{_kde_appsdir}/kolourpaint
%{_kde_iconsdir}/hicolor/*/apps/kolourpaint.*

#-----------------------------------------------------------------------------

%define kolourpaint_lgpl_major 4
%define libkolourpaint_lgpl %mklibname kolourpaint_lgpl %{kolourpaint_lgpl_major}

%package -n %{libkolourpaint_lgpl}
Summary:	Runtime library for Kolourpaint
Group:		System/Libraries

%description -n %{libkolourpaint_lgpl}
Runtime library for Kolourpaint.

%files -n %{libkolourpaint_lgpl}
%{_kde_libdir}/libkolourpaint_lgpl.so.%{kolourpaint_lgpl_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkolourpaint_lgpl} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_libdir}/libkolourpaint_lgpl.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Sat Jul 21 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Sat Jul 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.3-69.1mib2010.2
- New version 4.8.3
- Better summary
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.0-69.1mib2010.2
+ Revision: 762477
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762477
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758064
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 744545
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739303
- New upstream tarball $NEW_VERSION

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 731850
- New upstream tarball 4.7.80

* Mon Oct 10 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 703979
- Import kolourpaint
- Create kolourpaint folder

