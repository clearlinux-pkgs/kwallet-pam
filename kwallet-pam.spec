#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kwallet-pam
Version  : 5.27.7
Release  : 86
URL      : https://download.kde.org/stable/plasma/5.27.7/kwallet-pam-5.27.7.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.7/kwallet-pam-5.27.7.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.7/kwallet-pam-5.27.7.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1
Requires: kwallet-pam-data = %{version}-%{release}
Requires: kwallet-pam-lib = %{version}-%{release}
Requires: kwallet-pam-license = %{version}-%{release}
Requires: kwallet-pam-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : kwallet-dev
BuildRequires : libgcrypt-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
How kwallet-pam works:
During the pam "auth" (pam_authenticate) stage the module gets the password in plain text.
It hashes it against a random salt previously generated by kwallet of random data and keeps it in memory.

%package data
Summary: data components for the kwallet-pam package.
Group: Data

%description data
data components for the kwallet-pam package.


%package lib
Summary: lib components for the kwallet-pam package.
Group: Libraries
Requires: kwallet-pam-data = %{version}-%{release}
Requires: kwallet-pam-license = %{version}-%{release}

%description lib
lib components for the kwallet-pam package.


%package license
Summary: license components for the kwallet-pam package.
Group: Default

%description license
license components for the kwallet-pam package.


%package services
Summary: services components for the kwallet-pam package.
Group: Systemd services
Requires: systemd

%description services
services components for the kwallet-pam package.


%prep
%setup -q -n kwallet-pam-5.27.7
cd %{_builddir}/kwallet-pam-5.27.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690904617
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1690904617
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwallet-pam
cp %{_builddir}/kwallet-pam-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kwallet-pam/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kwallet-pam-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kwallet-pam/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kwallet-pam-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kwallet-pam/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/pam_kwallet_init

%files data
%defattr(-,root,root,-)
/usr/share/xdg/autostart/pam_kwallet_init.desktop

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/security/pam_kwallet5.so
/usr/lib64/security/pam_kwallet5.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwallet-pam/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/kwallet-pam/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kwallet-pam/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-kwallet-pam.service
