Summary:	Connections manager for GVFS
Name:		gigolo
Version:	0.4.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://files.uvena.de/gigolo/%{name}-%{version}.tar.bz2
# Source0-md5:	4abc6fde56572adf3ec3a0181092584c
URL:		http://www.uvena.de/gigolo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	gvfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gigolo is a frontend to easily manage connections to remote filesystems
using GIO/GVfs. It allows you to quickly connect/mount a remote
filesystem and manage bookmarks of such.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/gigolo
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gigolo
%{_desktopdir}/gigolo.desktop
%{_mandir}/man1/gigolo.1*

