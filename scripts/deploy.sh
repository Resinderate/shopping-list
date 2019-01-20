#!/usr/bin/env bash
sshpass -e ssh pi@kettle.mur-phy.com "supervisorctl restart kettlr"
