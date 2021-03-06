#!/usr/bin/bash

LOGS_PATH=$1
TEMP_FILE_PATH="/tmp/logFilesList"

if [[ -d $LOGS_PATH ]]; then
  # step1:
  ls -ld ${LOGS_PATH}/* | awk '{print $9}' | egrep '.*\.log$' > $TEMP_FILE_PATH
  # step2:
  cat $TEMP_FILE_PATH | xargs egrep -w -c '[_0-9]*ERROR[_0-9]*' | sed 's/:/ - /g'
  # NOTE: the ERROR regex is to avoid alphabetic words containing 'ERROR' unlike the work itself

  # rm -f $TEMP_FILE_PATH  # COMMENTED OUT IN CASE YOU"D LIKE TO EXAMINE THE TEMP FILE
else
  echo "ERROR: Couldn't find the directory under the path giver: $LOGS_PATH"
fi

# NOTE:
# IF I WERE ASKED AS A ONE-LINER [not per assignment specification]:
# ls -ld ${LOGS_PATH}/* | awk '{print $9}' | egrep '.*\.log$' | xargs egrep -w -c '[_0-9]*ERROR[_0-9]*' | sed 's/:/ - /g'