#!/usr/bin/env bash
cd "`dirname $0`/.."
git pull
pip3 install -r requirements.txt

export FLASK_APP=/home/pi/dev/shopping-list/shopping-list.py
flask run --host=0.0.0.0 --port=5001
