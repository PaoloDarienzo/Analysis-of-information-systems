#!/bin/bash

clear
echo START
echo cleaning coverage...
python-coverage erase
echo cleaning html...
rm -rf htmlcov
echo starting tests...

echo test_anno...
python-coverage run -p test_anno.py

echo test_calcolo...
python-coverage run -p test_calcolo.py

echo test_pasqua...
python-coverage run -p test_pasqua.py

echo combining...
python-coverage combine

echo printing report...
python-coverage report -m

echo creating html...
python-coverage html

rm src/pasqua.pyc
python-coverage erase
echo Done.
