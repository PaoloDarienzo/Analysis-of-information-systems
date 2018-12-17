#!/bin/bash

clear
echo START
echo cleaning coverage...
python-coverage erase
echo cleaning html...
rm -rf htmlcov
echo starting tests...

echo test_correttezza_insert...
python-coverage run -p test_correttezza_insert.py

echo test_calcolo_scaglione...
python-coverage run -p test_calcolo_scaglione.py

echo test_calcola_irpef...
python-coverage run -p test_calcola_irpef.py

echo test_irpef...
python-coverage run -p test_irpef.py

echo combining...
python-coverage combine

echo printing report...
python-coverage report -m

echo creating html...
python-coverage html

rm src/irpef.pyc
python-coverage erase
echo Done.
