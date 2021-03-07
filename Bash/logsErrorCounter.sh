#!/usr/bin/bash

LOGS_PATH=$1
TEMP_FILE_PATH="/tmp/logFilesList"
#LOGS_IN_PATH=$(ls -lhtr ${LOGS_PATH})
ls -lhtr > ${TEMP_FILE_PATH}
