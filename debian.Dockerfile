FROM ubuntu:20.04
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
  make \
  cmake \
  gcc \
  cmake-gui \
  cmake-curses-gui \
  doxygen \
  graphviz \
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
  libssl-dev \
  libxml2-dev \
  uuid-dev && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Before building the C++ library, first, build and install the Paho C library, if not already present. Note, this version of the C++ library requires Paho C v1.3.8 or greater.
RUN \
	git clone https://github.com/eclipse/paho.mqtt.c.git && \
	cd paho.mqtt.c && \
	git checkout v1.3.8 && \
	cmake -Bbuild -H. -DPAHO_ENABLE_TESTING=OFF -DPAHO_BUILD_STATIC=ON \ 
		-DPAHO_WITH_SSL=ON -DPAHO_HIGH_PERFORMANCE=ON && \
	cmake --build build/ --target install && \
	ldconfig

# build the Paho MQTT - C++ library
RUN \
	git clone https://github.com/eclipse/paho.mqtt.cpp && \
	cd paho.mqtt.cpp && \
	cmake -Bbuild -H. -DPAHO_BUILD_STATIC=ON -DPAHO_BUILD_DOCUMENTATION=TRUE -DPAHO_BUILD_SAMPLES=TRUE && \
	cmake --build build/ --target install && \
	ldconfig

# Build the debian package
#RUN \
#	cmake -Bbuild -H. -DPAHO_WITH_SSL=ON -DPAHO_ENABLE_TESTING=OFF -DPAHO_BUILD_DEB_PACKAGE=ON && \
#	cmake --build build && \
#	(cd build && cpack)	

COPY . .
RUN set -x && \
  mkdir build && cd build && \
  cmake -DCMAKE_INSTALL_PREFIX=${LIB_INSTALL_PREFIX} .. && make && make install

RUN set -x && \
  mkdir -p ${DEB_BUILD_DIR}/gvm-libs-22.4.0/usr/lib64 && \
  cp /usr/lib64/libgvm*.so.22.* ${DEB_BUILD_DIR}/gvm-libs-22.4.0/usr/lib64/ && \
  cd ${DEB_BUILD_DIR} && \
  tar -czvf gvm-libs_22.4.0.orig.tar.gz gvm-libs-22.4.0
COPY Debian ${DEB_BUILD_DIR}/gvm-libs-22.4.0
RUN set -x && \
  cd ${DEB_BUILD_DIR}/gvm-libs-22.4.0 && \
  debuild -us -uc
