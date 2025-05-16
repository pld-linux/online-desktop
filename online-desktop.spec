Summary:	Desktop built around web sites and online services
Summary(pl.UTF-8):	Pulpit zbudowany w oparciu o strony WWW i usługi online
Name:		online-desktop
Version:	0.3.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/online-desktop/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	90f27f4229c0a62c79e167de956b2eae
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gettext-tools
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libpurple-devel
BuildRequires:	libtool
BuildRequires:	nspr-devel >= 1:4.6.0
BuildRequires:	nss-devel >= 1:3.0.0
BuildRequires:	pidgin-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	bigboard
Requires:	firefox
Requires:	gnome-session
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "online desktop" is a flavor of the GNOME desktop built around web
sites and online services. This package contains a grab-bag of
integration points with various sites and services.

%description -l pl.UTF-8
"online desktop" to odmiana pulpitu GNOME zbudowana w oparciu o strony
WWW i usługi online. Ten pakiet zawiera pakiet punktów integracji z
różnymi stronami i usługami.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python\>$,%{__python},' \
	od-autostart od-reset od-session \
	mailto/od-mailto

%{__sed} -i -e '1s,/usr/bin/env python $,%{__python},' \
	presession/panel-config.py

%{__sed} -i -e '1s,/usr/bin/python$,%{__python},' \
	pyddm/ddm-viewer \
	weblogindriver/web-login-driver

%build
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/pidgin/libdbus-api-plugin.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/nssdecrypt.la

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install online-desktop.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall online-desktop.schemas

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ddm-viewer
%attr(755,root,root) %{_bindir}/od-autostart
%attr(755,root,root) %{_bindir}/od-mailto
%attr(755,root,root) %{_bindir}/od-reset
%attr(755,root,root) %{_bindir}/od-session
%attr(755,root,root) %{_bindir}/od-start-im
%attr(755,root,root) %{_bindir}/online-prefs-sync-daemon
%attr(755,root,root) %{_bindir}/web-login-driver
%attr(755,root,root) %{_libdir}/pidgin/libdbus-api-plugin.so
%{py_sitedir}/ddm
%{py_sitedir}/pyonlinedesktop
%{py_sitedir}/weblogindriver
%attr(755,root,root) %{py_sitedir}/nssdecrypt.so
%{_sysconfdir}/gconf/schemas/online-desktop.schemas
%{_desktopdir}/flickr.desktop
%{_desktopdir}/gmail.desktop
%{_desktopdir}/google-calendar.desktop
%{_desktopdir}/google-docs.desktop
%{_desktopdir}/google-reader.desktop
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/dbus-1/services/org.gnome.WebLoginDriver.service
%{_datadir}/gnome/autostart/online-desktop-autostart.desktop
%{_datadir}/gnome/autostart/online-prefs-sync.desktop
%{_datadir}/gnome/online-desktop.session
%{_iconsdir}/hicolor/*x*/apps/flickr.png
%{_iconsdir}/hicolor/*x*/apps/gmail.png
%{_iconsdir}/hicolor/*x*/apps/google-calendar.png
%{_iconsdir}/hicolor/*x*/apps/google-docs.png
%{_iconsdir}/hicolor/*x*/apps/google-reader.png
%{_iconsdir}/hicolor/*x*/apps/picasa.png
%{_iconsdir}/hicolor/*x*/apps/yahoo-mail.png
%dir %{_datadir}/online-desktop
%{_datadir}/online-desktop/autostart
%{_datadir}/online-desktop/gconf.xml.online-desktop
%dir %{_datadir}/online-desktop/presession
%attr(755,root,root) %{_datadir}/online-desktop/presession/panel-config.py
%{_datadir}/online-desktop/gconf.path
%dir %{_datadir}/online-prefs-sync
%{_datadir}/online-prefs-sync/online-prefs-sync.synclist
%{_datadir}/xsessions/online-desktop.desktop
