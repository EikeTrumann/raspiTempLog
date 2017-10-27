#!/bin/bash
# This script can collect the latest values from all temperature sensors
cd /home/pi/messungen/logs
echo "Current temperatures:" > latest.txt
date >> latest.txt

# each file in this folder contains the data from one sensor.
# this takes the last line of the log, reformats it and puts it into the current temperatures file 
for file in *.csv
do
	echo "${file^}" | cut -f1 -d'.' | sed 's/$/:/' - >> latest.txt
	tail -n 1 $file | cut -f1 -d';' | date | sed 's/^/\t/' - >> latest.txt
	tail -n 1 $file | cut -f2 -d';' | sed 's/.*/\t& mC/' - >> latest.txt
done
