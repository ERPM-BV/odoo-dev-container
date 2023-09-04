arg ODOO_VERSION=16.0
arg DOCKER_BASE_IMAGE=ghcr.io/kmagusiak/odoo-docker:${ODOO_VERSION}
from ${DOCKER_BASE_IMAGE} as vscode

# tools for development
user root
run apt-get update \
	&& apt-get install -y --no-install-recommends \
		libxml2-utils \
		bash-completion gettext git htop less openssh-client vim
add requirements-dev.txt /tmp
run cd /tmp \
	&& pip3 install --no-cache -r /tmp/requirements-dev.txt jupyterlab \
	&& rm -f /tmp/requirements-dev.txt

# use a single user for both running the container and devcontainer
arg DEV_UID=1000
run useradd --uid "${DEV_UID}" -G odoo --create-home vscode \
	&& echo "root:${ADMIN_PASSWORD:-admin}" | chpasswd \
	&& mkdir /odoo-workspace \
	&& chown vscode:odoo /odoo-workspace
user vscode
