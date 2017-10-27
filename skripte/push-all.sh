#!/bin/bash
ftp -v eiketrumann.de <<'EOT' > /home/pi/last-push.log // TODO change server
cd htdocs
lcd /home/pi/messungen/logs
prompt n
mput *
lcd /home/pi/messungen/plot
mput *
quit
EOT

