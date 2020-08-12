FROM centos:7.8.2003

# setup environment
ENV ZLIB_VERSION ${ZLIB_VERSION:-1.2.11}
ENV LIBGPG_ERROR_VERSION ${LIBGPG_ERROR_VERSION:-1.38}
ENV LIBASSUAN_VERSION ${LIBASSUAN_VERSION:-2.5.3}
ENV GPGME_VERSION ${GPGME_VERSION:-1.14.0}
ENV LIB_INSTALL_PREFIX ${LIB_INSTALL_PREFIX:-/}
ENV GVM_LIBS_RPM_BUILD_DIR ${GVM_LIBS_RPM_BUILD_DIR:-/root/gvm-libs/rpmbuild}
ENV ZLIB_DEVEL_RPM_BUILD_DIR ${ZLIB_DEVEL_RPM_BUILD_DIR:-/root/zlib-devel/rpmbuild}
ENV LIBGPG_ERROR_DEVEL_RPM_BUILD_DIR ${LIBGPG_ERROR_DEVEL_RPM_BUILD_DIR:-/root/libgpg-error/rpmbuild}
ENV LIBASSUAN_DEVEL_RPM_BUILD_DIR ${LIBASSUAN_DEVEL_RPM_BUILD_DIR:-/root/libassuan-error/rpmbuild}
ENV GPGME_DEVEL_RPM_BUILD_DIR ${GPGME_DEVEL_RPM_BUILD_DIR:-/root/gpgme-error/rpmbuild}

# install repositories
RUN yum -y install epel-release && \
  yum repolist

# install packages
RUN yum update -y && \
  yum install -q -y \
    wget \
    which \
    rpm-build \
    rpmlint \
    gnupg2-smime \
    tar \
    bzip2 \
    cmake3 \
    gcc \
    bison \
    glib2-devel \
    libgcrypt-devel \
    gnutls-devel \
    hiredis-devel \
    libssh-devel \
    libuuid-devel && \
  yum clean all && \
  rm -rf /var/cache/yum/*

# install missing packages from source
WORKDIR /tmp/zlib
RUN wget https://www.zlib.net/zlib-${ZLIB_VERSION}.tar.gz && \
  tar -xzvf zlib-${ZLIB_VERSION}.tar.gz --strip-components=1 && \
  ./configure --prefix=/ --libdir=/lib64 --includedir=/usr/include && make && make install
WORKDIR /tmp/libgpg-error
RUN wget https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-${LIBGPG_ERROR_VERSION}.tar.bz2 && \
  tar -jxvf libgpg-error-${LIBGPG_ERROR_VERSION}.tar.bz2 --strip-components=1 && \
  ./configure --prefix=/ --libdir=/lib64 --includedir=/usr/include && make && make install
WORKDIR /tmp/libassuan
RUN wget https://www.gnupg.org/ftp/gcrypt/libassuan/libassuan-${LIBASSUAN_VERSION}.tar.bz2 && \
  tar -jxvf libassuan-${LIBASSUAN_VERSION}.tar.bz2 --strip-components=1 && \
  ./configure --prefix=/ --libdir=/lib64 --includedir=/usr/include && make && make install
WORKDIR /tmp/gpgme
RUN wget https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-${GPGME_VERSION}.tar.bz2 && \
  tar -jxvf gpgme-${GPGME_VERSION}.tar.bz2 --strip-components=1 && \
  ./configure CC=c99 --prefix=/ --libdir=/lib64 --includedir=/usr/include && make && make install

# build gvm-libs
WORKDIR /tmp/gvm-libs
COPY . .
RUN set -x && \
  # need to do this in order to pass cmake tests; doesn't have any negative
  # consequences.
  sed -i 's/uuid>=2.25.0/uuid>=2.23.0/g' util/CMakeLists.txt && \
  # build as usual...
  mkdir build && cd build && \
  cmake3 -DCMAKE_INSTALL_PREFIX=${LIB_INSTALL_PREFIX} .. && make && make install

# build the RPM
WORKDIR ${GVM_LIBS_RPM_BUILD_DIR}
COPY RPM/gvm-libs/rpmbuild .
RUN set -x && \
  rpmbuild -bb SPECS/gvm-libs.spec
WORKDIR ${ZLIB_DEVEL_RPM_BUILD_DIR}
COPY RPM/devel/zlib-devel/rpmbuild .
RUN set -x && \
  rpmbuild -bb SPECS/zlib-devel.spec
WORKDIR ${LIBGPG_ERROR_DEVEL_RPM_BUILD_DIR}
COPY RPM/devel/libgpg-error-devel/rpmbuild .
RUN set -x && \
  rpmbuild -bb SPECS/libgpg-error-devel.spec
WORKDIR ${LIBASSUAN_DEVEL_RPM_BUILD_DIR}
COPY RPM/devel/libassuan-devel/rpmbuild .
RUN set -x && \
  rpmbuild -bb SPECS/libassuan-devel.spec
WORKDIR ${GPGME_DEVEL_RPM_BUILD_DIR}
COPY RPM/devel/gpgme-devel/rpmbuild .
RUN set -x && \
  rpmbuild -bb SPECS/gpgme-devel.spec