FROM ubuntu:18.04
ENV LIB_INSTALL_PREFIX ${LIB_INSTALL_PREFIX:-/usr}
ENV DEB_BUILD_DIR ${DEB_BUILD_DIR:-/tmp/gvm-libs}
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -q -y --fix-missing \
  autotools-dev \
  build-essential \
  tar \
  devscripts \
  debhelper \
  clang \
  clang-format \
  cmake \
  gcc \
  pkg-config \
  bison \
  libglib2.0-dev \
  libgpgme-dev \
  libgcrypt20-dev \
  libgnutls28-dev \
  libhiredis-dev \
  libnet1-dev \
  libpcap-dev \
  libssh-gcrypt-dev \
  libxml2-dev \
  uuid-dev && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*
COPY . .
RUN set -x && \
  mkdir build && cd build && \
  cmake -DCMAKE_INSTALL_PREFIX=${LIB_INSTALL_PREFIX} .. && make && make install
RUN set -x && \
  mkdir -p ${DEB_BUILD_DIR}/gvm-libs-21.4.4/usr/lib && \
  cp /usr/lib/libgvm*.so.21.* ${DEB_BUILD_DIR}/gvm-libs-21.4.4/usr/lib/ && \
  cd ${DEB_BUILD_DIR} && \
  tar -czvf gvm-libs_21.4.4.orig.tar.gz gvm-libs-21.4.4
COPY Debian ${DEB_BUILD_DIR}/gvm-libs-21.4.4
RUN set -x && \
  cd ${DEB_BUILD_DIR}/gvm-libs-21.4.4 && \
  debuild -us -uc
