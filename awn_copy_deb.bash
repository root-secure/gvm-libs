#!/bin/bash

DEB_BUILD_DIR=/tmp/gvm-libs
IMAGE="$1"
echo IMAGE == "$IMAGE"
docker run -it ${IMAGE} /bin/true
LATEST=$(docker ps -l -f ancestor=${IMAGE} --format "{{.ID}}")
docker cp ${LATEST}:${DEB_BUILD_DIR}/gvm-libs_10.0.2_amd64.deb ./
for dock in $(docker ps -f ancestor=${IMAGE} -a -q) ; do
	docker rm $dock
done
