#!/usr/bin/env bash

rm -rf venv
python3 -m venv ./venv
source venv/bin/activate
pip install wheel
pip install -r src/requirements.txt
pip install -r requirements-test.txt