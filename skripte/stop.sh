kill $(cat /home/pi/messungen/config/pid)
rm /home/pi/messungen/config/pid
datename=`date '+%m-%d-%H-%M'`
mkdir /home/pi/messungen/logs/${datename}/
mv /home/pi/messungen/logs/*.csv /home/pi/messungen/logs/${datename}/
