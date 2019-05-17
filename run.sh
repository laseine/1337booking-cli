#!/bin/bash
path=$0
if [[ $(readlink $path) ]]; then
	path=$(readlink $path)
fi

cd "$(dirname "$path")"

source bin/activate
/usr/bin/env python3 booking-cli $@
