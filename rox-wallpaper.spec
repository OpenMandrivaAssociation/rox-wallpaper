%define name rox-wallpaper
%define oname wallpaper
%define version 2.1
%define release %mkrel 5
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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.1-5mdv2010.0
+ Revision: 433428
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.1-4mdv2009.0
+ Revision: 242561
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Aug 04 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.1-1mdv2007.0
- Rebuild

* Mon Jan 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.1-1mdk
- New release 2.1
- use mkrel

* Mon Aug 29 2005 Götz Waschk <waschk@mandriva.org> 2.0-1mdk
- update file list
- new version

* Wed Aug 24 2005 Götz Waschk <waschk@mandriva.org> 1.9.2-3mdk
- drop prefix

* Fri Aug 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.9.2-2mdk
- rebuild

