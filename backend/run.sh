#!/bin/bash

# kill any existing scrapyd process if any
kill -9 $(pidof scrapyd)

# enter directory where configure file lies and launch scrapyd
cd /home/backend/spider_tophub && nohup scrapyd >& /dev/null &

cd /home/backend/api_tophub && export FLASK_APP=run.py && flask run --port=5000 --host=0.0.0.0