#!/bin/bash
CWD="$(cd $(dirname $0) && pwd)"
EXTRA_OPTS=""

cat << EOF >/etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.33.132 mongo1
192.168.33.133 mongo2
192.168.33.134 mongo3
EOF

echo 'StrictHostKeyChecking no' >/root/.ssh/config

ansible-playbook ${EXTRA_OPTS} -i ${CWD}/hosts ${CWD}/site.yml \
--extra-vars "http_proxy=${http_proxy} https_proxy=${https_proxy}"

exit 0
