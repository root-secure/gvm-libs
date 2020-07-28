FROM ubuntu:18.04
ENV LIB_INSTALL_PREFIX ${LIB_INSTALL_PREFIX:-/usr}
ENV DEB_BUILD_DIR ${DEB_BUILD_DIR:-/tmp/gvm-libs}
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -q -y --fix-missing \
  tar \
  devscripts \
  debhelper \
  cmake \
  gcc \
  pkg-config \
  bison \
  libglib2.0-dev \
  libgpgme-dev \
  libgcrypt20-dev \
  libgnutls28-dev \
  libhiredis-dev \
  libssh-gcrypt-dev \
  uuid-dev && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*
COPY . .
RUN set -x && \
  mkdir build && cd build && \
  cmake -DCMAKE_INSTALL_PREFIX=${LIB_INSTALL_PREFIX} .. && make && make install
RUN set -x && \
  mkdir -p ${DEB_BUILD_DIR}/gvm-libs-10.0.2/usr/lib && \
  cp /usr/lib/libgvm*.so.10.0.* ${DEB_BUILD_DIR}/gvm-libs-10.0.2/usr/lib/ && \
  cd ${DEB_BUILD_DIR} && \
  tar -czvf gvm-libs_10.0.2.orig.tar.gz gvm-libs-10.0.2
COPY Debian ${DEB_BUILD_DIR}/gvm-libs-10.0.2
RUN set -x && \
  cd ${DEB_BUILD_DIR}/gvm-libs-10.0.2 && \
  debuild -us -uc
