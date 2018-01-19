#!/bin/bash
echo "@@@ Install ansible"
pip install PyYAML paramiko Jinja2 httplib2 six
pip install ansible
yum install -y sshpass

echo "@@@ Done!"

exit 0
