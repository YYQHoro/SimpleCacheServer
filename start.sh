#!/bin/bash
CUR_PATH=$(dirname $(realpath "$0"))
kill $(cat $CUR_PATH/pid)
nohup python3 $CUR_PATH/simple_cache_server.py --port 5001 >$CUR_PATH/run.log 2>&1 & echo $! > $CUR_PATH/pid
exit 0