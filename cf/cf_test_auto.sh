#!/bin/bash

clear
echo START
echo cleaning coverage...
python-coverage erase
echo cleaning html...
rm -rf htmlcov
echo starting tests...

echo test_date...
python-coverage run -p test_date.py

echo test_string...
python-coverage run -p test_string.py

echo test_codici...
python-coverage run -p test_codici.py

echo test_cf...
python-coverage run -p test_cf.py

echo combining...
python-coverage combine

echo printing report...
python-coverage report -m

echo creating html...
python-coverage html

rm src/codice_fiscale.pyc
python-coverage erase
echo Done.
