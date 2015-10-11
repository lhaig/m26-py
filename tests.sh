#!/bin/bash

echo 'running all tests with nose and code coverage...'

source bin/activate

nosetests --with-coverage --cover-html --cover-html-dir=coverage --cover-package=m26
