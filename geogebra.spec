%define		geoversion 3-2-45-0
Summary:	GeoGebra is dynamic mathematics software
Name:		geogebra
Version:	3.2.45.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://geogebra.googlecode.com/files/GeoGebra-MacOS-Installer-%{geoversion}.zip
# Source0-md5:	5d39c2c225e0085a88001f7eac5ff324
Source10:	%{name}
# source11 taken from archlinux
Source11:	%{name}.desktop
Source12:	http://aur.archlinux.org/packages/geogebra/geogebra/%{name}.png
# Source12-md5:	e324ee3a2bb438cee625e3f29770a315
URL:		http://www.geogebra.org
Requires:	jre >= 1.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoGebra is dynamic mathematics software for all levels of education
that joins arithmetic, geometry, algebra and calculus. It offers
multiple representations of objects in its graphics, algebra, and
spreadsheet views that are all dynamically linked.

%prep
%setup -q -n GeoGebra.app

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}/geogebra/unsigned
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install Contents/Resources/Java/*.jar $RPM_BUILD_ROOT%{_javadir}/geogebra
install Contents/Resources/Java/unsigned/*.jar $RPM_BUILD_ROOT%{_javadir}/geogebra

install %{SOURCE10} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE11} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE12} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
