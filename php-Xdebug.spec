#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
#
Name     : php-Xdebug
Version  : 3.1.5
Release  : 37
URL      : https://pecl.php.net/get/xdebug-3.1.5.tgz
Source0  : https://pecl.php.net/get/xdebug-3.1.5.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
BuildRequires : buildreq-php
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Xdebug
======
.. image:: https://github.com/xdebug/xdebug/workflows/Build/badge.svg
:target: https://github.com/xdebug/xdebug/actions?query=workflow%3ABuild
.. image:: https://ci.appveyor.com/api/projects/status/glp9xfsmt1p25nkn?svg=true
:target: https://ci.appveyor.com/project/derickr/xdebug
.. image:: https://circleci.com/gh/xdebug/xdebug/tree/master.svg?style=svg
:target: https://circleci.com/gh/xdebug/xdebug

%prep
%setup -q -n xdebug-3.1.5
cd %{_builddir}/xdebug-3.1.5
pushd ..
cp -a xdebug-3.1.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-Xdebug
cp %{_builddir}/xdebug-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-Xdebug/b854c7a41498334267d60c530714fa37952d1dd6 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
