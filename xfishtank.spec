Summary:	An X Window System graphic display of an animated aquarium
Summary(pl):	Program pod X wy¶wietlaj±cy animowane akwarium
Name:		xfishtank
Version:	2.1tp
Release:	3
License:	MIT
Group:		X11/Amusements
Source0:	http://metalab.unc.edu/pub/Linux/X11/demos/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
The xfishtank program displays an animated aquarium background on your
screen. Xfishtank works with the X Window System.

%description -l pl
Program xfishtank wy¶wietla na ekranie t³o z animowanym akwarium.
Dzia³a z X Window System.

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
