Name:           gpgme-devel
Version:        1.14.0
Release:        1%{?dist}
Group:          Development/Libraries
Summary:        Development headers and libraries for gpgme

License:        LGPLv2+
URL:            http://www.gnupg.org/related_software/gpgme/
Source:         https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-1.14.0.tar.bz2
Vendor:         CentOS

ExclusiveArch:  x86_64

BuildRoot:      /tmp/rpmbuild

%description
Development headers and libraries for gpgme

%install
mkdir -p %{buildroot}/opt/awn/bin
mkdir -p %{buildroot}/opt/awn/usr/include
mkdir -p %{buildroot}/opt/awn/lib64/pkgconfig
mkdir -p %{buildroot}/opt/awn/share
mkdir -p %{buildroot}/opt/awn/share/aclocal
mkdir -p %{buildroot}/opt/awn/share/common-lisp/source/gpgme
mkdir -p %{buildroot}/opt/awn/share/info
mkdir -p %{buildroot}/etc/ld.so.conf.d
cp /bin/gpgme-config %{buildroot}/opt/awn/bin/
cp /bin/gpgme-json %{buildroot}/opt/awn/bin/
cp /bin/gpgme-tool %{buildroot}/opt/awn/bin/
cp /usr/include/gpgme.h %{buildroot}/opt/awn/usr/include/gpgme.h
cp /lib64/libgpgme.la %{buildroot}/opt/awn/lib64/
ln -s /lib64/libgpgme.so.11.23.0 %{buildroot}/opt/awn/lib64/libgpgme.so
ln -s /lib64/libgpgme.so.11.23.0 %{buildroot}/opt/awn/lib64/libgpgme.so.11
cp /lib64/libgpgme.so.11.23.0 %{buildroot}/opt/awn/lib64/
cp /lib64/pkgconfig/gpgme-glib.pc %{buildroot}/opt/awn/lib64/pkgconfig/
cp /lib64/pkgconfig/gpgme.pc %{buildroot}/opt/awn/lib64/pkgconfig/
cp /share/aclocal/gpgme.m4 %{buildroot}/opt/awn/share/aclocal/
cp /share/common-lisp/source/gpgme/gpgme-grovel.lisp %{buildroot}/opt/awn/share/common-lisp/source/gpgme/
cp /share/common-lisp/source/gpgme/gpgme-package.lisp %{buildroot}/opt/awn/share/common-lisp/source/gpgme/
cp /share/common-lisp/source/gpgme/gpgme.asd %{buildroot}/opt/awn/share/common-lisp/source/gpgme/
cp /share/common-lisp/source/gpgme/gpgme.lisp %{buildroot}/opt/awn/share/common-lisp/source/gpgme/
cp /share/info/dir %{buildroot}/opt/awn/share/info/
cp /share/info/gpgme.info %{buildroot}/opt/awn/share/info/
cp /share/info/gpgme.info-1 %{buildroot}/opt/awn/share/info/
cp /share/info/gpgme.info-2 %{buildroot}/opt/awn/share/info/
cp /ld.so.conf %{buildroot}/etc/ld.so.conf.d/gpgme.conf

%files
/opt/awn/bin/gpgme-config
/opt/awn/bin/gpgme-json
/opt/awn/bin/gpgme-tool
/opt/awn/usr/include/gpgme.h
/opt/awn/lib64/libgpgme.la
/opt/awn/lib64/libgpgme.so
/opt/awn/lib64/libgpgme.so.11
/opt/awn/lib64/libgpgme.so.11.23.0
/opt/awn/lib64/pkgconfig/gpgme-glib.pc
/opt/awn/lib64/pkgconfig/gpgme.pc
/opt/awn/share/aclocal/gpgme.m4
/opt/awn/share/common-lisp/source/gpgme/gpgme-grovel.lisp
/opt/awn/share/common-lisp/source/gpgme/gpgme-package.lisp
/opt/awn/share/common-lisp/source/gpgme/gpgme.asd
/opt/awn/share/common-lisp/source/gpgme/gpgme.lisp
/opt/awn/share/info/dir
/opt/awn/share/info/gpgme.info
/opt/awn/share/info/gpgme.info-1
/opt/awn/share/info/gpgme.info-2
/etc/ld.so.conf.d/gpgme.conf

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
