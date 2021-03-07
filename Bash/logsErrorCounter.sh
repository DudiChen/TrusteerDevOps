#!/usr/bin/bash

LOGS_PATH=$1
echo $1
TEMP_FILE_PATH="/tmp/logFilesList"
#LOGS_IN_PATH=$(ls -lhtr ${LOGS_PATH})
ls -ld ${LOGS_PATH}/* | awk '{print $9}' | egrep '.*\.log$' > $TEMP_FILE_PATH
cat $TEMP_FILE_PATH | xargs egrep -w -c '[_0-9]*ERROR[_0-9]*' | sed 's/:/ - /g'
# rm -f $TEMP_FILE_PATH  # COMMENTED OUT IN CASE YOU"D LIKE TO EXAMINE THE TEMP FILE

# NOTE:
# IF I WERE ASKED AS A ONE-LINER [not per assignment specification]:
# ls -ld ${LOGS_PATH}/* | awk '{print $9}' | egrep '.*\.log$' | xargs egrep -w -c '[_0-9]*ERROR[_0-9]*' | sed 's/:/ - /g'