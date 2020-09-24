Name:           libuuid-devel
Version:        2.36.0
Release:        1%{?dist}
Group:          Development/Libraries
Summary:        Universally unique ID library

License:        BSD
URL:            http://en.wikipedia.org/wiki/Util-linux
Source:         https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/v2.36/util-linux-2.36.tar.gz
Vendor:         CentOS

ExclusiveArch:  x86_64

BuildRoot:      /tmp/rpmbuild

%description
This is the universally unique ID development library and headers,
part of util-linux.
.
The libuuid library generates and parses 128-bit universally unique
id's (UUID's).  A UUID is an identifier that is unique across both
space and time, with respect to the space of all UUIDs.  A UUID can
be used for multiple purposes, from tagging objects with an extremely
short lifetime, to reliably identifying very persistent objects
across a network.

%install
mkdir -p %{buildroot}/opt/awn/usr/include/uuid/
mkdir -p %{buildroot}/opt/awn/lib64/pkgconfig
mkdir -p %{buildroot}/opt/awn/share/man/man3
mkdir -p %{buildroot}/etc/ld.so.conf.d
cp /usr/include/uuid/uuid.h %{buildroot}/opt/awn/usr/include/uuid/
cp /lib64/libuuid.la %{buildroot}/opt/awn/lib64/
cp /lib64/libuuid.so.1.3.0 %{buildroot}/opt/awn/lib64/
ln -s /lib64/libuuid.so.1.3.0 %{buildroot}/opt/awn/lib64/libuuid.so
ln -s /lib64/libuuid.so.1.3.0 %{buildroot}/opt/awn/lib64/libuuid.so.1
cp /share/man/man3/uuid.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_clear.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_compare.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_copy.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_generate.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_generate_random.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_generate_time.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_generate_time_safe.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_is_null.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_parse.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_time.3 %{buildroot}/opt/awn/share/man/man3/
cp /share/man/man3/uuid_unparse.3 %{buildroot}/opt/awn/share/man/man3/
cp /ld.so.conf %{buildroot}/etc/ld.so.conf.d/libuuid.conf

%files
/opt/awn/usr/include/uuid/uuid.h
/opt/awn/lib64/libuuid.la
/opt/awn/lib64/libuuid.so
/opt/awn/lib64/libuuid.so.1
/opt/awn/lib64/libuuid.so.1.3.0
/opt/awn/share/man/man3/uuid.3
/opt/awn/share/man/man3/uuid_clear.3
/opt/awn/share/man/man3/uuid_compare.3
/opt/awn/share/man/man3/uuid_copy.3
/opt/awn/share/man/man3/uuid_generate.3
/opt/awn/share/man/man3/uuid_generate_random.3
/opt/awn/share/man/man3/uuid_generate_time.3
/opt/awn/share/man/man3/uuid_generate_time_safe.3
/opt/awn/share/man/man3/uuid_is_null.3
/opt/awn/share/man/man3/uuid_parse.3
/opt/awn/share/man/man3/uuid_time.3
/opt/awn/share/man/man3/uuid_unparse.3
/etc/ld.so.conf.d/libuuid.conf

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
-
