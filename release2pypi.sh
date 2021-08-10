#!/bin/sh

if [ -d "./sdist" ]; then
    rm -r sdist
fi
if [ -d "./dist" ]; then
    rm -r dist
fi

echo "package project..."
python setup.py sdist
echo "start upload..."
python -m twine upload -u FDSEKG -p FDSEKG#401 dist/*.tar.gz