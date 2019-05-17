#!/bin/bash

cd "$(dirname "$path")"

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

echo -n "Do you want to install booking-cli globally (requires root)? [y/N]"
read ans
if [[ $ans != "y" ]]; then
	echo "Installation finished."
	exit;
fi

sudo ln -s ./run.sh /usr/bin/booking-cli

