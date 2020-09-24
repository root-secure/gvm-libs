Name:           zlib-devel
Version:        1.2.11
Release:        1%{?dist}
Group:          Development/Libraries
Summary:        Header files and libraries for Zlib development

License:        zlib and Boost
URL:            http://www.zlib.net/
Source:         https://www.zlib.net/zlib-1.2.11.tar.gz
Vendor:         CentOS

ExclusiveArch:  x86_64

BuildRoot:      /tmp/rpmbuild

%description
The zlib-devel package contains the header files and libraries needed
to develop programs that use the zlib compression and decompression
library.

%install
mkdir -p %{buildroot}/opt/awn/lib64/pkgconfig
mkdir -p %{buildroot}/opt/awn/usr/include
mkdir -p %{buildroot}/opt/awn/share/man/man3/
mkdir -p %{buildroot}/etc/ld.so.conf.d
cp /lib64/libz.a %{buildroot}/opt/awn/lib64/
ln -s /opt/awn/lib64/libz.so.1.2.11 %{buildroot}/opt/awn/lib64/libz.so
ln -s /opt/awn/lib64/libz.so.1.2.11 %{buildroot}/opt/awn/lib64/libz.so.1
cp /lib64/libz.so.1.2.11 %{buildroot}/opt/awn/lib64/
cp /lib64/pkgconfig/zlib.pc %{buildroot}/opt/awn/lib64/pkgconfig/zlib.pc
cp /usr/include/zconf.h %{buildroot}/opt/awn/usr/include/
cp /usr/include/zlib.h %{buildroot}/opt/awn/usr/include/
cp /share/man/man3/zlib.3 %{buildroot}/opt/awn/share/man/man3/
cp /ld.so.conf %{buildroot}/etc/ld.so.conf.d/zlib.conf

%files
/opt/awn/lib64/libz.a
/opt/awn/lib64/libz.so
/opt/awn/lib64/libz.so.1
/opt/awn/lib64/libz.so.1.2.11
/opt/awn/lib64/pkgconfig/zlib.pc
/opt/awn/usr/include/zconf.h
/opt/awn/usr/include/zlib.h
/opt/awn/share/man/man3/zlib.3
/etc/ld.so.conf.d/zlib.conf

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
