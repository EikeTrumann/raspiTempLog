#!/bin/bash

nohup python /home/pi/messungen/python/log_data.py &> /dev/null &
echo $! > /home/pi/messungen/config/pid
date +'%s' > /home/pi/messungen/config/start
