Summary:	An X Window System graphic display of an animated aquarium.
Name:		xfishtank
Version:	2.1tp
Release:	2
Copyright:	MIT
Group:		Amusements/Graphics
Source:		http://metalab.unc.edu/pub/Linux/X11/demos/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
The xfishtank program displays an animated aquarium background on your
screen.  Xfishtank works with the X Window System.

%prep
%setup -q

%build
xmkmf
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfishtank
