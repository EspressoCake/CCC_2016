#!/bin/bash

apt-get update > /dev/null 2&>1
apt-get install aria2
pip install -r ./Python/requirements.txt
python ./Python/CCC_Grab.py

