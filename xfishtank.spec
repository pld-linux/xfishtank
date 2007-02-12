Summary:	An X Window System graphic display of an animated aquarium
Summary(pl.UTF-8):   Program pod X wyświetlający animowane akwarium
Name:		xfishtank
Version:	2.1tp
Release:	3
License:	MIT
Group:		X11/Amusements
Source0:	http://www.ibiblio.org/pub/Linux/X11/demos/%{name}-%{version}.tar.gz
# Source0-md5:	a8e1efd1f2cd96aafde4fc105a4ed4c2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
The xfishtank program displays an animated aquarium background on your
screen. Xfishtank works with the X Window System.

%description -l pl.UTF-8
Program xfishtank wyświetla na ekranie tło z animowanym akwarium.
Działa z X Window System.

%prep
%setup -q

%build
xmkmf
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfishtank
