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
mkdir -p %{buildroot}/opt/awn/bin
mkdir -p %{buildroot}/opt/awn/usr/include
mkdir -p %{buildroot}/opt/awn/lib64
mkdir -p %{buildroot}/opt/awn/lib64/pkgconfig
mkdir -p %{buildroot}/opt/awn/share
mkdir -p %{buildroot}/opt/awn/share/aclocal
mkdir -p %{buildroot}/opt/awn/share/common-lisp
mkdir -p %{buildroot}/opt/awn/share/common-lisp/source/
mkdir -p %{buildroot}/opt/awn/share/common-lisp/source/gpg-error
mkdir -p %{buildroot}/opt/awn/share/info
mkdir -p %{buildroot}/opt/awn/share/libgpg-error
mkdir -p %{buildroot}/opt/awn/share/locale
mkdir -p %{buildroot}/opt/awn/share/locale/cs/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/da/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/de/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/eo/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/es/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/fr/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/hu/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/it/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/ja/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/nl/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/pl/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/pt/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/ro/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/ru/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/sr/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/sv/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/uk/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/vi/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/zh_CN/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/locale/zh_TW/LC_MESSAGES
mkdir -p %{buildroot}/opt/awn/share/man/man1
mkdir -p %{buildroot}/etc/ld.so.conf.d
cp /bin/gpg-error %{buildroot}/opt/awn/bin/
cp /bin/gpg-error-config %{buildroot}/opt/awn/bin/
cp /bin/gpgrt-config %{buildroot}/opt/awn/bin/
cp /bin/yat2m %{buildroot}/opt/awn/bin/
cp /usr/include/gpg-error.h %{buildroot}/opt/awn/usr/include/
cp /usr/include/gpgrt.h %{buildroot}/opt/awn/usr/include/
cp /lib64/libgpg-error.la %{buildroot}/opt/awn/lib64/
ln -s /lib64/libgpg-error.so.0.29.0 %{buildroot}/opt/awn/lib64/libgpg-error.so
ln -s /lib64/libgpg-error.so.0.29.0 %{buildroot}/opt/awn/lib64/libgpg-error.so.0
cp /lib64/libgpg-error.so.0.29.0 %{buildroot}/opt/awn/lib64/
cp /lib64/pkgconfig/gpg-error.pc %{buildroot}/opt/awn/lib64/pkgconfig/
cp /share/aclocal/gpg-error.m4 %{buildroot}/opt/awn/share/aclocal/
cp /share/aclocal/gpgrt.m4 %{buildroot}/opt/awn/share/aclocal/
cp /share/common-lisp/source/gpg-error/gpg-error-codes.lisp %{buildroot}/opt/awn/share/common-lisp/source/gpg-error/
cp /share/common-lisp/source/gpg-error/gpg-error-package.lisp %{buildroot}/opt/awn/share/common-lisp/source/gpg-error/
cp /share/common-lisp/source/gpg-error/gpg-error.asd %{buildroot}/opt/awn/share/common-lisp/source/gpg-error/
cp /share/common-lisp/source/gpg-error/gpg-error.lisp %{buildroot}/opt/awn/share/common-lisp/source/gpg-error/
cp /share/info/dir %{buildroot}/opt/awn/share/info/
cp /share/info/gpgrt.info %{buildroot}/opt/awn/share/info/
cp /share/libgpg-error/errorref.txt %{buildroot}/opt/awn/share/libgpg-error/
cp /share/locale/cs/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/cs/LC_MESSAGES/
cp /share/locale/da/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/da/LC_MESSAGES/
cp /share/locale/de/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/de/LC_MESSAGES/
cp /share/locale/eo/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/eo/LC_MESSAGES/
cp /share/locale/es/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/es/LC_MESSAGES/
cp /share/locale/fr/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/fr/LC_MESSAGES/
cp /share/locale/hu/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/hu/LC_MESSAGES/
cp /share/locale/it/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/it/LC_MESSAGES/
cp /share/locale/ja/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/ja/LC_MESSAGES/
cp /share/locale/nl/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/nl/LC_MESSAGES/
cp /share/locale/pl/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/pl/LC_MESSAGES/
cp /share/locale/pt/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/pt/LC_MESSAGES/
cp /share/locale/ro/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/ro/LC_MESSAGES/
cp /share/locale/ru/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/ru/LC_MESSAGES/
cp /share/locale/sr/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/sr/LC_MESSAGES/
cp /share/locale/sv/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/sv/LC_MESSAGES/
cp /share/locale/uk/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/uk/LC_MESSAGES/
cp /share/locale/vi/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/vi/LC_MESSAGES/
cp /share/locale/zh_CN/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/zh_CN/LC_MESSAGES/
cp /share/locale/zh_TW/LC_MESSAGES/libgpg-error.mo %{buildroot}/opt/awn/share/locale/zh_TW/LC_MESSAGES/
cp /share/man/man1/gpgrt-config.1 %{buildroot}/opt/awn/share/man/man1/
cp /ld.so.conf %{buildroot}/etc/ld.so.conf.d/libgpg-error.conf

%files
/opt/awn/bin/gpg-error
/opt/awn/bin/gpg-error-config
/opt/awn/bin/gpgrt-config
/opt/awn/bin/yat2m
/opt/awn/usr/include/gpg-error.h
/opt/awn/usr/include/gpgrt.h
/opt/awn/lib64/libgpg-error.la
/opt/awn/lib64/libgpg-error.so
/opt/awn/lib64/libgpg-error.so.0
/opt/awn/lib64/libgpg-error.so.0.29.0
/opt/awn/lib64/pkgconfig/gpg-error.pc
/opt/awn/share/aclocal/gpg-error.m4
/opt/awn/share/aclocal/gpgrt.m4
/opt/awn/share/common-lisp/source/gpg-error/gpg-error-codes.lisp
/opt/awn/share/common-lisp/source/gpg-error/gpg-error-package.lisp
/opt/awn/share/common-lisp/source/gpg-error/gpg-error.asd
/opt/awn/share/common-lisp/source/gpg-error/gpg-error.lisp
/opt/awn/share/info/dir
/opt/awn/share/info/gpgrt.info
/opt/awn/share/libgpg-error/errorref.txt
/opt/awn/share/locale/cs/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/da/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/de/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/eo/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/es/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/fr/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/hu/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/it/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/ja/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/nl/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/pl/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/pt/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/ro/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/ru/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/sr/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/sv/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/uk/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/vi/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/zh_CN/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/locale/zh_TW/LC_MESSAGES/libgpg-error.mo
/opt/awn/share/man/man1/gpgrt-config.1
/etc/ld.so.conf.d/libgpg-error.conf

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
