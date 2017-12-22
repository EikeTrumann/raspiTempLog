#!/bin/bash
touch cron.template

# This are the parts of the crontab entry
cronbase='''* * * * *''' # Update every minute
basename=$(dirname $BASH_SOURCE)
cd $basename
basename=$(pwd)
scriptname="update.sh"

# This is the line that should be in the crontab file
echo "$cronbase $basename/$scriptname" > cron.template
crontab cron.template
rm cron.template

# Make the update script executable
chmod +x update.sh
chmod +x before-update.sh
chmod +x after-update.sh