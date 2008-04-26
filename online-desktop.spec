Summary:	Desktop built around web sites and online services
Name:		online-desktop
Version:	0.2.28
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/online-desktop/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	79789b90f671008192b8e42ca5514447
URL:		http://online-desktop.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libtool
BuildRequires:	nspr-devel >= 1:4.6.0
BuildRequires:	nss-devel >= 1:3.0.0
BuildRequires:	pidgin-libs
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,preun):	GConf2
Requires:	bigboard
Requires:	gnome-session
Requires:	mozilla-firefox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "online desktop" is a flavor of the GNOME desktop built around web
sites and online services. This package contains a grab-bag of
integration points with various sites and services.

%prep
%setup -q

%build
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

rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/libdbus-api-plugin.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/nssdecrypt.la

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
%attr(755,root,root) %{_bindir}/ddm-viewer
%attr(755,root,root) %{_bindir}/od-autostart
%attr(755,root,root) %{_bindir}/od-mailto
%attr(755,root,root) %{_bindir}/od-reset
%attr(755,root,root) %{_bindir}/od-session
%attr(755,root,root) %{_bindir}/od-start-im
%attr(755,root,root) %{_bindir}/online-prefs-sync-daemon
%attr(755,root,root) %{_bindir}/web-login-driver
%attr(755,root,root) %{_libdir}/pidgin/libdbus-api-plugin.so
%dir %{py_sitedir}/ddm
%{py_sitedir}/ddm/*.py[co]
%attr(755,root,root) %{py_sitedir}/nssdecrypt.so
%dir %{py_sitedir}/pyonlinedesktop
%{py_sitedir}/pyonlinedesktop/*.py[co]
%{_sysconfdir}/gconf/schemas/online-desktop.schemas
%{_desktopdir}/flickr.desktop
%{_desktopdir}/gmail.desktop
%{_desktopdir}/google-calendar.desktop
%{_desktopdir}/google-docs.desktop
%{_desktopdir}/google-reader.desktop
%{_datadir}/dbus-1/services/org.gnome.WebLoginDriver.service
%{_datadir}/gnome/autostart/online-desktop-autostart.desktop
%{_datadir}/gnome/autostart/online-prefs-sync.desktop
%{_datadir}/gnome/online-desktop.session
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/online-desktop
%dir %{_datadir}/online-prefs-sync
%{_datadir}/online-prefs-sync/online-prefs-sync.synclist
%{_datadir}/xsessions/online-desktop.desktop
