#!/bin/bash

if [[ $EUID == 0 ]]; then
	echo "Do not run this as root."
	exit;
fi

if ! [[ $(which python3) ]]; then
	echo "Python3 must be installed.";
	exit;
fi

echo "Checking pip3..."
if ! [[ $(which pip3) ]]; then
	echo "pip3 doesn't exist, installing pip3...";
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python3 get-pip.py
	rm get-pip.py
fi

echo "Configuring environment..."
pip3 install virtualenv

virtualenv -p python3 .
source bin/activate
pip3 install -r requirements.txt
