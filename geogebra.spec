Summary:	GeoGebra is dynamic mathematics software
Name:		geogebra
Version:	3.2.34
Release:	0.1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.geogebra.org/webstart/unpacked/%{version}/unpacked/%{name}.jar
# Source0-md5:	e275dd6a7a46ce65dbc39e4f7dbf27b6
Source1:	http://www.geogebra.org/webstart/unpacked/%{version}/unpacked/%{name}_cas.jar
# Source1-md5:	05b38af666109b1971b935c4779b340e
Source2:	http://www.geogebra.org/webstart/unpacked/%{version}/unpacked/%{name}_export.jar
# Source2-md5:	2b9f74784f1234d4d1c4f7d4c4cdffc4
Source3:	http://www.geogebra.org/webstart/unpacked/%{version}/unpacked/%{name}_gui.jar
# Source3-md5:	91a3039fd613b07b18d545c444778a9f
Source4:	http://www.geogebra.org/webstart/unpacked/%{version}/unpacked/%{name}_main.jar
# Source4-md5:	08434d4739809da3b426554f57100d30
Source5:	http://www.geogebra.org/webstart/unpacked/%{version}/unpacked/%{name}_properties.jar
# Source5-md5:	0e36d2c1f7e03ecdf3c22af80fa02ae9
Source10:	%{name}
# source11 taken from archlinux
Source11:	%{name}.desktop
Source12:	http://aur.archlinux.org/packages/geogebra/geogebra/%{name}.png
# Source12-md5:	e324ee3a2bb438cee625e3f29770a315
URL:		http://www.geogebra.org
Requires:	java-sun-jre >= 1.4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoGebra is dynamic mathematics software for all levels of education
that joins arithmetic, geometry, algebra and calculus. It offers
multiple representations of objects in its graphics, algebra, and
spreadsheet views that are all dynamically linked.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}/geogebra
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT%{_javadir}/geogebra
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
