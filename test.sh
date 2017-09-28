#!/bin/bash

source bin/activate

echo 'checking the source code with flake8 ...'
flake8 m26 --ignore F401

echo 'running all tests with nose and code coverage...'
nosetests --with-coverage --cover-html --cover-html-dir=coverage --cover-package=m26
