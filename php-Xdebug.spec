#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v26
# autospec commit: 99a7985
#
Name     : php-Xdebug
Version  : 3.4.3
Release  : 78
URL      : https://pecl.php.net/get/xdebug-3.4.3.tgz
Source0  : https://pecl.php.net/get/xdebug-3.4.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-Xdebug-lib = %{version}-%{release}
Requires: php-Xdebug-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : file
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

%package lib
Summary: lib components for the php-Xdebug package.
Group: Libraries
Requires: php-Xdebug-license = %{version}-%{release}

%description lib
lib components for the php-Xdebug package.


%package license
Summary: license components for the php-Xdebug package.
Group: Default

%description license
license components for the php-Xdebug package.


%prep
%setup -q -n xdebug-3.4.3
cd %{_builddir}/xdebug-3.4.3
pushd ..
cp -a xdebug-3.4.3 buildavx2
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
cp %{_builddir}/xdebug-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-Xdebug/ef03b875be47757078fb328a54833bab8bbfc594 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20240924/xdebug.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-Xdebug/ef03b875be47757078fb328a54833bab8bbfc594
