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
mkdir -p %{buildroot}/opt/awn/bin
mkdir -p %{buildroot}/opt/awn/usr/include
mkdir -p %{buildroot}/opt/awn/lib64
mkdir -p %{buildroot}/opt/awn/lib64/pkgconfig
mkdir -p %{buildroot}/opt/awn/share
mkdir -p %{buildroot}/opt/awn/share/aclocal
mkdir -p %{buildroot}/opt/awn/share/info
mkdir -p %{buildroot}/etc/ld.so.conf.d
cp /bin/libassuan-config %{buildroot}/opt/awn/bin/
cp /usr/include/assuan.h %{buildroot}/opt/awn/usr/include/
cp /lib64/libassuan.la %{buildroot}/opt/awn/lib64/
ln -s /opt/awn/lib64/libassuan.so.0.8.3 %{buildroot}/opt/awn/lib64/libassuan.so
ln -s /opt/awn/lib64/libassuan.so.0.8.3 %{buildroot}/opt/awn/lib64/libassuan.so.0
cp /lib64/libassuan.so.0.8.3 %{buildroot}/opt/awn/lib64/
cp /lib64/pkgconfig/libassuan.pc %{buildroot}/opt/awn/lib64/pkgconfig/
cp /share/aclocal/libassuan.m4 %{buildroot}/opt/awn/share/aclocal/
cp /share/info/assuan.info %{buildroot}/opt/awn/share/info/
cp /share/info/dir %{buildroot}/opt/awn/share/info/
cp /ld.so.conf %{buildroot}/etc/ld.so.conf.d/libassuan.conf

%files
/opt/awn/bin/libassuan-config
/opt/awn/usr/include/assuan.h
/opt/awn/lib64/libassuan.la
/opt/awn/lib64/libassuan.so
/opt/awn/lib64/libassuan.so.0
/opt/awn/lib64/libassuan.so.0.8.3
/opt/awn/lib64/pkgconfig/libassuan.pc
/opt/awn/share/aclocal/libassuan.m4
/opt/awn/share/info/assuan.info
/opt/awn/share/info/dir
/etc/ld.so.conf.d/libassuan.conf

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
