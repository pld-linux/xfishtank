Summary: An X Window System graphic display of an animated aquarium.
Name: xfishtank
Version: 2.0
Release: 14
Copyright: MIT
Group: Amusements/Graphics
Source: ftp://ftp.x.org/R5contrib/xfishtank.tar.Z
Patch: xfishtank-bugs.patch
BuildRoot: /var/tmp/xfishtank-root

%description
The xfishtank program displays an animated aquarium background on your
screen.  Xfishtank works with the X Window System.

%prep
%setup -q -n xfishtank
%patch -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xfishtank
