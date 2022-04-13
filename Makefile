

all: package_deb

.PHONY: package_deb get_sudo clean

DOCKER_TAG=awn-gvm-libs

NEED_SUDO=$(shell [ -e /var/run/docker.sock -a ! -w /var/run/docker.sock ] && echo -n YES || echo -n NO)
HAS_SUDO=$(shell sudo -n cat - </dev/null 2>/dev/null && echo -n YES || echo -n NO)
SUDO:=
ifeq "${NEED_SUDO}" "YES"
	SUDO:=sudo
endif

get_sudo:
ifeq "${NEED_SUDO}" "YES"
ifeq "${HAS_SUDO}" "NO"
	@echo "It appears as though 'docker build' requires sudo access (/var/run/docker.sock "
	@echo "exists and is not writable). As a result, you will be prompted to enter your "
	@echo "credentials for sudo. Please provide them when asked."
endif
endif

package_deb: get_sudo
	@${SUDO} docker build --no-cache=true -t ${DOCKER_TAG}:deb_builder -f debian.Dockerfile .
	@${SUDO} ./awn_copy_deb.bash ${DOCKER_TAG}:deb_builder

clean:
	@rm -vf *_amd64.deb
