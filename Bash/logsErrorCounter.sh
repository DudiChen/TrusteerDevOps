#!/usr/bin/bash

LOGS_PATH=$1
echo $1
TEMP_FILE_PATH="/tmp/logFilesList"
#LOGS_IN_PATH=$(ls -lhtr ${LOGS_PATH})
ls -l $LOGS_PATH | grep *.log | awk '{print $9}' > ${TEMP_FILE_PATH}
