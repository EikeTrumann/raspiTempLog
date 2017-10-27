wget http://ipinfo.io/ip -qO - > ip.txt
date > lastonline.txt

ftp -v eiketrumann.de <<'EOT' // TODO URL
cd htdocs
send ip.txt
send lastonline.txt
quit
EOT

rm ip.txt
rm lastonline.txt

