#!/bin/bash
echo "@@@ Install python-pip"
yum groupinstall -y "Base"
yum groupinstall -y "Development tools"
yum install -y zlib zlib-devel openssl tk-devel tcl-devel sqlite-devel ncurses-devel gdbm-devel readline-devel bzip2-devel db4-devel openssl-devel python-setuptools python-devel
yum install -y libffi-devel

easy_install pip
pip install --upgrade pip

echo "Done!"

exit 0
