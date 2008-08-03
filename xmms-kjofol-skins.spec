%define name xmms-kjofol-skins
%define pluginname kint_xmms
%define version 1.2.0
%define plugversion 0.95
%define release %mkrel 11

Name: %{name}
Summary: XMMS - Vis plugin to get kjofol skins + some kjofol skins
Version: %{version}
Release: %{release}
Source0: http://www.csse.monash.edu.au/~timf/%{pluginname}-%{plugversion}.tar.gz
Source1: kjofol-skins.tar.bz2
Patch0: kint_xmms-0.94.patch
Patch1: xmms-kj-pic.patch
Patch2: xmms-kj-64bit-fixes.patch
License: GPL
Group: Sound
URL: http://www.dgs.monash.edu.au/~timf/xmms/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: xmms >= 1.2.0 unzip
BuildRequires: gtk+-devel libxmms-devel libpng-devel

%description
In this package you can find the Visualization plugin that enable K-Jofol skins
support, and several cute K-Jofol skins.

%prep
%setup -q -a 1 -n xmms-kj
%patch0 -p1
%patch1 -p1 -b .pic
%patch2 -p1 -b .64bit-fixes

%build
make vislib

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xmms/Visualization
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xmms/kjofol
make LIBDIR=$RPM_BUILD_ROOT%{_libdir}/xmms/Visualization install-vislib
install -m644 default.zip kjofol/* $RPM_BUILD_ROOT%{_datadir}/xmms/kjofol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING readme.txt
%{_libdir}/xmms/Visualization/libkjofol*
%{_datadir}/xmms/kjofol/

