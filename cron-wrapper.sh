#!/bin/bash
# Wrapper script to run from crontab

WORKDIR="/home/automation/TenableAWS"
SCRIPT="TenableAWS-Updater.py"
LOGFILE="/var/log/aws-tenableaws.log"

echo "Running TenableAWS..."
cd ${WORKDIR}
/usr/bin/python ${SCRIPT} > ${LOGFILE}
