Name:           libgpg-error-devel
Version:        1.38
Release:        1%{?dist}
Group:          Development/Libraries
Summary:        Development files for the libgpg-error package

License:        LGPLv2+
URL:            ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source:         https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.38.tar.bz2
Vendor:         CentOS

ExclusiveArch:  x86_64

BuildRoot:      /tmp/rpmbuild

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future. This package
contains files necessary to develop applications using libgpg-error.

%install
mkdir %{buildroot}/bin
mkdir -p %{buildroot}/usr/include
mkdir %{buildroot}/lib64
mkdir %{buildroot}/lib64/pkgconfig
mkdir %{buildroot}/share
mkdir %{buildroot}/share/aclocal
mkdir %{buildroot}/share/common-lisp
mkdir %{buildroot}/share/common-lisp/source/
mkdir %{buildroot}/share/common-lisp/source/gpg-error
mkdir %{buildroot}/share/info
mkdir %{buildroot}/share/libgpg-error
mkdir %{buildroot}/share/locale
mkdir -p %{buildroot}/share/locale/cs/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/da/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/de/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/eo/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/es/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/fr/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/hu/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/it/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/ja/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/nl/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/pl/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/pt/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/ro/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/ru/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/sr/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/sv/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/uk/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/vi/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/zh_CN/LC_MESSAGES
mkdir -p %{buildroot}/share/locale/zh_TW/LC_MESSAGES
mkdir -p %{buildroot}/share/man/man1
cp /bin/gpg-error %{buildroot}/bin/
cp /bin/gpg-error-config %{buildroot}/bin/
cp /bin/gpgrt-config %{buildroot}/bin/
cp /bin/yat2m %{buildroot}/bin/
cp /usr/include/gpg-error.h %{buildroot}/usr/include/
cp /usr/include/gpgrt.h %{buildroot}/usr/include/
cp /lib64/libgpg-error.la %{buildroot}/lib64/
ln -s /lib64/libgpg-error.so.0.29.0 %{buildroot}/lib64/libgpg-error.so
ln -s /lib64/libgpg-error.so.0.29.0 %{buildroot}/lib64/libgpg-error.so.0
cp /lib64/libgpg-error.so.0.29.0 %{buildroot}/lib64/
cp /lib64/pkgconfig/gpg-error.pc %{buildroot}/lib64/pkgconfig/
cp /share/aclocal/gpg-error.m4 %{buildroot}/share/aclocal/
cp /share/aclocal/gpgrt.m4 %{buildroot}/share/aclocal/
cp /share/common-lisp/source/gpg-error/gpg-error-codes.lisp %{buildroot}/share/common-lisp/source/gpg-error/
cp /share/common-lisp/source/gpg-error/gpg-error-package.lisp %{buildroot}/share/common-lisp/source/gpg-error/
cp /share/common-lisp/source/gpg-error/gpg-error.asd %{buildroot}/share/common-lisp/source/gpg-error/
cp /share/common-lisp/source/gpg-error/gpg-error.lisp %{buildroot}/share/common-lisp/source/gpg-error/
cp /share/info/dir %{buildroot}/share/info/
cp /share/info/gpgrt.info %{buildroot}/share/info/
cp /share/libgpg-error/errorref.txt %{buildroot}/share/libgpg-error/
cp /share/locale/cs/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/cs/LC_MESSAGES/
cp /share/locale/da/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/da/LC_MESSAGES/
cp /share/locale/de/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/de/LC_MESSAGES/
cp /share/locale/eo/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/eo/LC_MESSAGES/
cp /share/locale/es/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/es/LC_MESSAGES/
cp /share/locale/fr/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/fr/LC_MESSAGES/
cp /share/locale/hu/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/hu/LC_MESSAGES/
cp /share/locale/it/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/it/LC_MESSAGES/
cp /share/locale/ja/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/ja/LC_MESSAGES/
cp /share/locale/nl/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/nl/LC_MESSAGES/
cp /share/locale/pl/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/pl/LC_MESSAGES/
cp /share/locale/pt/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/pt/LC_MESSAGES/
cp /share/locale/ro/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/ro/LC_MESSAGES/
cp /share/locale/ru/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/ru/LC_MESSAGES/
cp /share/locale/sr/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/sr/LC_MESSAGES/
cp /share/locale/sv/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/sv/LC_MESSAGES/
cp /share/locale/uk/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/uk/LC_MESSAGES/
cp /share/locale/vi/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/vi/LC_MESSAGES/
cp /share/locale/zh_CN/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/zh_CN/LC_MESSAGES/
cp /share/locale/zh_TW/LC_MESSAGES/libgpg-error.mo %{buildroot}/share/locale/zh_TW/LC_MESSAGES/
cp /share/man/man1/gpgrt-config.1 %{buildroot}/share/man/man1/ 

%files
/bin/gpg-error
/bin/gpg-error-config
/bin/gpgrt-config
/bin/yat2m
/usr/include/gpg-error.h
/usr/include/gpgrt.h
/lib64/libgpg-error.la
/lib64/libgpg-error.so
/lib64/libgpg-error.so.0
/lib64/libgpg-error.so.0.29.0
/lib64/pkgconfig/gpg-error.pc
/share/aclocal/gpg-error.m4
/share/aclocal/gpgrt.m4
/share/common-lisp/source/gpg-error/gpg-error-codes.lisp
/share/common-lisp/source/gpg-error/gpg-error-package.lisp
/share/common-lisp/source/gpg-error/gpg-error.asd
/share/common-lisp/source/gpg-error/gpg-error.lisp
/share/info/dir
/share/info/gpgrt.info
/share/libgpg-error/errorref.txt
/share/locale/cs/LC_MESSAGES/libgpg-error.mo
/share/locale/da/LC_MESSAGES/libgpg-error.mo
/share/locale/de/LC_MESSAGES/libgpg-error.mo
/share/locale/eo/LC_MESSAGES/libgpg-error.mo
/share/locale/es/LC_MESSAGES/libgpg-error.mo
/share/locale/fr/LC_MESSAGES/libgpg-error.mo
/share/locale/hu/LC_MESSAGES/libgpg-error.mo
/share/locale/it/LC_MESSAGES/libgpg-error.mo
/share/locale/ja/LC_MESSAGES/libgpg-error.mo
/share/locale/nl/LC_MESSAGES/libgpg-error.mo
/share/locale/pl/LC_MESSAGES/libgpg-error.mo
/share/locale/pt/LC_MESSAGES/libgpg-error.mo
/share/locale/ro/LC_MESSAGES/libgpg-error.mo
/share/locale/ru/LC_MESSAGES/libgpg-error.mo
/share/locale/sr/LC_MESSAGES/libgpg-error.mo
/share/locale/sv/LC_MESSAGES/libgpg-error.mo
/share/locale/uk/LC_MESSAGES/libgpg-error.mo
/share/locale/vi/LC_MESSAGES/libgpg-error.mo
/share/locale/zh_CN/LC_MESSAGES/libgpg-error.mo
/share/locale/zh_TW/LC_MESSAGES/libgpg-error.mo
/share/man/man1/gpgrt-config.1

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
