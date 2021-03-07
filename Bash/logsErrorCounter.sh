#!/usr/bin/bash

LOGS_PATH=$1
echo $1
TEMP_FILE_PATH="/tmp/logFilesList"
#LOGS_IN_PATH=$(ls -lhtr ${LOGS_PATH})
ls -lhtr $LOGS_PATH > ${TEMP_FILE_PATH}
