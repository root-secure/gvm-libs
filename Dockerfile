FROM debian:latest
ENV GVM_LIBS_VERSION ${GVM_LIBS_VERSION:-v10.0.1}
ENV LIB_INSTALL_PREFIX ${LIB_INSTALL_PREFIX:-/usr}
ENV DEB_BUILD_DIR ${DEB_BUILD_DIR:-/tmp/gvm-libs}
COPY . .
RUN apt-get update && apt-get install -q -y --fix-missing \
  wget \
  tar \
  devscripts \
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
RUN set -x && \
  mkdir build && cd build && \
  cmake -DCMAKE_INSTALL_PREFIX=${LIB_INSTALL_PREFIX} .. && make && make install
RUN set -x && \
  mkdir -p ${DEB_BUILD_DIR}/gvm-libs-10.0.1/usr/lib && \
  cp /usr/lib/libgvm*.so.10.0.1 ${DEB_BUILD_DIR}/gvm-libs-10.0.1/usr/lib/ && \
  tar -C ${DEB_BUILD_DIR} -czvf gvm-libs_10.0.1.orig.tar.gz gvm-libs-10.0.1
COPY Debian /tmp/gvm-libs/gvm-libs-10.0.1
RUN set -x && \
  cd ${DEB_BUILD_DIR}/gvm-libs-10.0.1 && \
  debuild -us -uc
