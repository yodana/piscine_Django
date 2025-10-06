#!/bin/bash
# Faire source setup.sh
python3 -m venv django_env
source django_env/bin/activate
pip install -r requirement.txt --break-system-packages # A enlever pour 42