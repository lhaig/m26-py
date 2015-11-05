#!/bin/bash

# Shell script to install or upgrade python packages for this pyvenv.
# Chris Joakim, 2015/11/05

source bin/activate

pip install --upgrade pip
pip install --upgrade pip-tools

pip-compile requirements.in
pip install -r requirements.txt
pip-sync

pip list > pip_list.txt

echo 'done'
