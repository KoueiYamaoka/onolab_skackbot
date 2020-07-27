#/bin/bash

fpath='/datanet/kyamaoka/slackbot/end_report.py'

if [ $# = 1 ]; then
    python $fpath "$1"
else
    python $fpath "$1" -n "$2"
fi
