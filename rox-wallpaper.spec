%define name rox-wallpaper
%define oname wallpaper
%define version 2.1
%define release %mkrel 2
%define appdir %_prefix/lib/apps
Summary: Set the wallpaper image for the ROX graphical desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/rox/%{oname}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/Other
URL: http://rox.sf.net/wallpaper.html
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: rox-lib
Buildarch: noarch

%description
This program can be used to set the background image for your pinboard, if
you are using ROX-Filer 1.3.1 or later to manage it. Use an older version of
Wallpaper to set the background with older versions of the filer.

Note that ROX-Filer already allows you to set an image or plain colour for
the backdrop. Wallpaper lets you do more interesting things...

%prep
%setup -q -n %oname-%version
chmod 644 Wallpaper/Wallpaper.xml
%build

%install
rm -rf $RPM_BUILD_ROOT %name.lang
mkdir -p %buildroot/%appdir
cp -r Wallpaper %buildroot/%appdir
rm -rf %buildroot/%appdir/Wallpaper/Messages/*.po
rm -rf %buildroot/%appdir/Wallpaper/Messages/dist
rm -rf %buildroot/%appdir/Wallpaper/Messages/update-po
for gmo in %buildroot%appdir/Wallpaper/Messages/*.gmo;do
echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%buildroot!!)" >> %name.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc %appdir/Wallpaper/Help
%dir %appdir/Wallpaper
%appdir/Wallpaper/.DirIcon
%appdir/Wallpaper/*.py
%appdir/Wallpaper/App*
%appdir/Wallpaper/Wallpaper.xml

