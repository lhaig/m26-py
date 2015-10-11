#!/bin/bash

# Shell script to install or upgrade python packages for this pyvenv.
# Chris Joakim, 2015/10/11

source bin/activate

echo 'upgrading pip and libraries used by this project...'

pip install --upgrade pip

pip3 --version
python3 --version

pip install --upgrade nose
pip install --upgrade coverage
pip install --upgrade check-manifest

pip list   > pip_list.txt
pip freeze > requirements.txt

echo 'done'

# Captured output from this script:
# upgrading pip and libraries used by this project...
# Requirement already up-to-date: pip in ./lib/python3.5/site-packages
# pip 7.1.2 from /Users/cjoakim/github/m26-py/lib/python3.5/site-packages (python 3.5)
# Python 3.5.0
# Requirement already up-to-date: nose in ./lib/python3.5/site-packages
# Requirement already up-to-date: coverage in ./lib/python3.5/site-packages
# Requirement already up-to-date: check-manifest in ./lib/python3.5/site-packages
# done
