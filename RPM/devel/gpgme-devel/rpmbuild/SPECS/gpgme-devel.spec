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
mkdir %{buildroot}/bin
mkdir -p %{buildroot}/usr/include
mkdir -p %{buildroot}/lib64/pkgconfig
mkdir %{buildroot}/share
mkdir %{buildroot}/share/aclocal
mkdir -p %{buildroot}/share/common-lisp/source/gpgme
mkdir %{buildroot}/share/info
cp /bin/gpgme-config %{buildroot}/bin/
cp /bin/gpgme-json %{buildroot}/bin/
cp /bin/gpgme-tool %{buildroot}/bin/
cp /usr/include/gpgme.h %{buildroot}/usr/include/gpgme.h
cp /lib64/libgpgme.la %{buildroot}/lib64/
ln -s /lib64/libgpgme.so.11.23.0 %{buildroot}/lib64/libgpgme.so
ln -s /lib64/libgpgme.so.11.23.0 %{buildroot}/lib64/libgpgme.so.11
cp /lib64/libgpgme.so.11.23.0 %{buildroot}/lib64/
cp /lib64/pkgconfig/gpgme-glib.pc %{buildroot}/lib64/pkgconfig/
cp /lib64/pkgconfig/gpgme.pc %{buildroot}/lib64/pkgconfig/
cp /share/aclocal/gpgme.m4 %{buildroot}/share/aclocal/
cp /share/common-lisp/source/gpgme/gpgme-grovel.lisp %{buildroot}/share/common-lisp/source/gpgme/
cp /share/common-lisp/source/gpgme/gpgme-package.lisp %{buildroot}/share/common-lisp/source/gpgme/
cp /share/common-lisp/source/gpgme/gpgme.asd %{buildroot}/share/common-lisp/source/gpgme/
cp /share/common-lisp/source/gpgme/gpgme.lisp %{buildroot}/share/common-lisp/source/gpgme/
cp /share/info/dir %{buildroot}/share/info/
cp /share/info/gpgme.info %{buildroot}/share/info/
cp /share/info/gpgme.info-1 %{buildroot}/share/info/
cp /share/info/gpgme.info-2 %{buildroot}/share/info/

%files
/bin/gpgme-config
/bin/gpgme-json
/bin/gpgme-tool
/usr/include/gpgme.h
/lib64/libgpgme.la
/lib64/libgpgme.so
/lib64/libgpgme.so.11
/lib64/libgpgme.so.11.23.0
/lib64/pkgconfig/gpgme-glib.pc
/lib64/pkgconfig/gpgme.pc
/share/aclocal/gpgme.m4
/share/common-lisp/source/gpgme/gpgme-grovel.lisp
/share/common-lisp/source/gpgme/gpgme-package.lisp
/share/common-lisp/source/gpgme/gpgme.asd
/share/common-lisp/source/gpgme/gpgme.lisp
/share/info/dir
/share/info/gpgme.info
/share/info/gpgme.info-1
/share/info/gpgme.info-2

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
