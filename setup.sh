#!/bin/bash
echo ''

virtualenv -p /usr/bin/python2.7 envs/python2
echo ''

virtualenv -p /usr/local/bin/python3 envs/python3
echo ''

source envs/python3/bin/activate
pip install -r riskmetrics/requirements.txt
echo ''

python riskmetrics/mirror_nvd.py
echo ''

python riskmetrics/get_scanner.py
echo ''

./scancode-toolkit-1.6.0/scancode --help
echo ''

