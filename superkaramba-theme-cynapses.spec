
%define		theme	cynapses

Summary:	superkaramba - cynapses theme
Summary(pl):	superkaramba - motyw cynapses
Name:		superkaramba-theme-%{theme}
Version:	1
Release:	0.4
License:	GPL
Group:		Themes
Source0:	11405-cynapses_karamba.tar.bz2
# Source0-md5:	450fdaab9af75def0d87e920492b284f
Patch0:		%{name}-osinfo.patch
URL:		http://www.kde-look.org/content/show.php?content=11405
Requires:	issue
Requires:	lm_sensors
Requires:	superkaramba
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cynapses theme for superkaramba.

%description -l pl
Motyw cynapses do superkaramby.

%prep
%setup -q -c
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/cynapses_karamba/{font,img,scripts}  \
    	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/cynapses_karamba/img/icons

install cynapses_karamba/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/cynapses_karamba/
install cynapses_karamba/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/cynapses_karamba/
install cynapses_karamba/font/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/cynapses_karamba/font
install cynapses_karamba/img/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/cynapses_karamba/img
install cynapses_karamba/img/icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/cynapses_karamba/img/icons
install cynapses_karamba/scripts/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/cynapses_karamba/scripts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/themes/superkaramba/cynapses_karamba
%dir %{_datadir}/themes/superkaramba/cynapses_karamba/font
%dir %{_datadir}/themes/superkaramba/cynapses_karamba/img
%dir %{_datadir}/themes/superkaramba/cynapses_karamba/scripts
%dir %{_datadir}/themes/superkaramba/cynapses_karamba/img/icons
%{_datadir}/themes/superkaramba/cynapses_karamba/*.png
%{_datadir}/themes/superkaramba/cynapses_karamba/*.theme
%{_datadir}/themes/superkaramba/cynapses_karamba/font/*
%{_datadir}/themes/superkaramba/cynapses_karamba/img/*.png
%{_datadir}/themes/superkaramba/cynapses_karamba/img/icons/*.png
%attr(755,root,root) %{_datadir}/themes/superkaramba/cynapses_karamba/scripts/*
