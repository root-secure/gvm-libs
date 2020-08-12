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
mkdir -p %{buildroot}/lib64/pkgconfig
mkdir -p %{buildroot}/usr/include
mkdir -p %{buildroot}/share/man/man3/
cp /lib64/libz.a %{buildroot}/lib64/
cp /lib64/libz.so %{buildroot}/lib64/
cp /lib64/libz.so.1 %{buildroot}/lib64/
cp /lib64/libz.so.1.2.11 %{buildroot}/lib64/
cp /lib64/pkgconfig/zlib.pc %{buildroot}/lib64/pkgconfig/zlib.pc
cp /usr/include/zconf.h %{buildroot}/usr/include/
cp /usr/include/zlib.h %{buildroot}/usr/include/
cp /share/man/man3/zlib.3 %{buildroot}/share/man/man3/

%files
/lib64/libz.a
/lib64/libz.so
/lib64/libz.so.1
/lib64/libz.so.1.2.11
/lib64/pkgconfig/zlib.pc
/usr/include/zconf.h
/usr/include/zlib.h
/share/man/man3/zlib.3

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
