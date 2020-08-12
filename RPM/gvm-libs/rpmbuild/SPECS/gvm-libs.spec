Name:           gvm-libs
Version:        10.0.2
Release:        1%{?dist}
Group:          System Environment/Libraries
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server

License:        GPLv2+
URL:            http://www.openvas.org
Source:         https://github.com/greenbone/gvm-libs/archive/v10.0.2.tar.gz
Vendor:         Greenbone https://www.greenbone.net

ExclusiveArch:  x86_64

BuildRoot:      /tmp/rpmbuild

%description
This is the libraries module for the Greenbone Vulnerability Management
Solution.
.
It is used for the Greenbone Security Manager appliances and provides various
functionalities to support the integrated service daemons.

%install
mkdir -p %{buildroot}/lib64/pkgconfig
cp /lib64/pkgconfig/libgvm_base.pc %{buildroot}/lib64/pkgconfig/libgvm_base.pc
cp /lib64/libgvm*.so.10.0.2 %{buildroot}/lib64/

%files
/lib64/pkgconfig/libgvm_base.pc
/lib64/libgvm_base.so.10.0.2
/lib64/libgvm_util.so.10.0.2
/lib64/libgvm_osp.so.10.0.2
/lib64/libgvm_gmp.so.10.0.2

%changelog
* Wed Aug 5 2020 aschryver Arctic Wolf Networks
