%define oname wallpaper
%define appdir %{_prefix}/lib/apps

Summary:   Set the wallpaper image for the ROX graphical desktop

Name:      rox-wallpaper
Version:   2.3
Release:   1
Source0:   https://sourceforge.net/projects/rox/files/Wallpaper/2.3/Wallpaper-%{version}.tar.gz
License:   GPL
Group:     Graphical desktop/Other
URL:       http://rox.sf.net/wallpaper.html
Requires:  rox-lib
BuildArch: noarch

%description
This program can be used to set the background image for your pinboard, if
you are using ROX-Filer 1.3.1 or later to manage it. Use an older version of
Wallpaper to set the background with older versions of the filer.

Note that ROX-Filer already allows you to set an image or plain colour for
the backdrop. Wallpaper lets you do more interesting things...

%prep
%setup -qc
chmod 644 Wallpaper/Wallpaper.xml

%build

%install
rm -rf %{buildroot} %{name}.lang
mkdir -p %{buildroot}/%{appdir}
cp -r Wallpaper %{buildroot}/%{appdir}
rm -rf %{buildroot}/%{appdir}/Wallpaper/Messages/*.po
rm -rf %{buildroot}/%{appdir}/Wallpaper/Messages/dist
rm -rf %{buildroot}/%{appdir}/Wallpaper/Messages/update-po
for gmo in %{buildroot}%{appdir}/Wallpaper/Messages/*.gmo;do
echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%{buildroot}!!)" >> %{name}.lang
done

%clean

%files -f %{name}.lang
%doc %{appdir}/Wallpaper/Help
%dir %{appdir}/Wallpaper
%{appdir}/Wallpaper/.DirIcon
%{appdir}/Wallpaper/*.py
%{appdir}/Wallpaper/App*
%{appdir}/Wallpaper/Wallpaper.xml
%{appdir}/Wallpaper/Messages/messages.pot
%{appdir}/Wallpaper/makedist.sh

