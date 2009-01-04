
# -*- RPM-SPEC -*-
Summary: Graphical utility which allows you to manage cluster configuration
Name: system-config-cluster
Version: 1.0.53
Release: %mkrel 1
URL: http://www.redhat.com/
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python-gnome, pygtk2.0, pygtk2.0-libglade, gnome-python-canvas, gnome-python-gnomevfs
Requires: rhpl >= 0.148.2
Requires: python >= 2.3
BuildRequires: perl(XML::Parser) gettext

%description
system-config-cluster is a utility which allows you to manage cluster configuration in a graphical setting.

%prep
%setup -q
perl -pi -e 's,(/usr/bin/python)\S*,$1,g' src/ModelBuilder.py src/system-config-cluster.py
perl -pi -e 's/auth(\s*)required(\s*)pam_stack.so service=/auth${1}include${2}/g' system-config-cluster.pam

%build
%configure
make

%install
rm -rf %{buildroot}
%makeinstall

#Uncomment this when translations are done
#%find_lang %name

%clean
rm -rf %{buildroot}

#Replace the files line with the one commented out when translations are done
#%files -f %{name}.lang
%files

%defattr(-,root,root)
%doc COPYING
#%doc docs/ReleaseNotes
#%doc docs/html/*
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/applications/system-config-cluster.desktop
%{_datadir}/system-config-cluster
%config %{_sysconfdir}/pam.d/system-config-cluster
%config %{_sysconfdir}/security/console.apps/system-config-cluster

