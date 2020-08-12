Name:           libassuan-devel
Version:        2.5.3
Release:        1%{?dist}
Group:          Development/Libraries
Summary:        GnuPG IPC library

License:        LGPLv2+ and GPLv3+
URL:            http://www.gnupg.org/
Source:         https://www.gnupg.org/ftp/gcrypt/libassuan/libassuan-2.5.3.tar.bz2
Vendor:         CentOS

ExclusiveArch:  x86_64

BuildRoot:      /tmp/rpmbuild

%description
This is the IPC static library used by GnuPG 2, GPGME and a few other
packages.
.
This package contains files needed to develop applications using libassuan.

%install
mkdir %{buildroot}/bin
mkdir -p %{buildroot}/usr/include
mkdir %{buildroot}/lib64
mkdir %{buildroot}/lib64/pkgconfig
mkdir %{buildroot}/share
mkdir %{buildroot}/share/aclocal
mkdir %{buildroot}/share/info
cp /bin/libassuan-config %{buildroot}/bin/
cp /usr/include/assuan.h %{buildroot}/usr/include/
cp /lib64/libassuan.la %{buildroot}/lib64/
ln -s /lib64/libassuan.so.0.8.3 %{buildroot}/lib64/libassuan.so
ln -s /lib64/libassuan.so.0.8.3 %{buildroot}/lib64/libassuan.so.0
cp /lib64/libassuan.so.0.8.3 %{buildroot}/lib64/
cp /lib64/pkgconfig/libassuan.pc %{buildroot}/lib64/pkgconfig/
cp /share/aclocal/libassuan.m4 %{buildroot}/share/aclocal/
cp /share/info/assuan.info %{buildroot}/share/info/
cp /share/info/dir %{buildroot}/share/info/

%files
/bin/libassuan-config
/usr/include/assuan.h
/lib64/libassuan.la
/lib64/libassuan.so
/lib64/libassuan.so.0
/lib64/libassuan.so.0.8.3
/lib64/pkgconfig/libassuan.pc
/share/aclocal/libassuan.m4
/share/info/assuan.info
/share/info/dir

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
