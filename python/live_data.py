import time
import sys

if not len(sys.argv) == 2:
	print "Es muss der Name oder die ID eines Sensors als Argument gegeben werden"
	sys.exit()

# Namen des Sensors
if sys.argv[1][0] == '2' and sys.argv[1][1] == '8':
	id = sys.argv[1]
else:
	name = sys.argv[1]
	# Konfigurationsdatei oeffnen
	configfile = open("/home/pi/messungen/config/sensoren",'r')
	config = configfile.readlines()
	configfile.close()
	# Jede Konfigurationszeile ist ein Sensorname mit ID 
	for line in config:
		line = line.split(' ')
		if line[0] == name:
			id = line[1].rstrip()
			break
		print "Der Sensorname konnte nicht in der Konfiguration gefunden werden"
		sys.exit()

# busy-loop zur schnellstmoeglichen Messdatenerfassung
while 1:
	# Datei oeffnen
	ausgabe = open("/sys/bus/w1/devices/"+id+"/w1_slave").readlines()
	# Die ersten 10 Bloecke in der Datei sind die hexadezimalen Daten
	ausgabe[0] = ausgabe[0].split(' ')[11]
	# Hinter dem T steht die Temperatur
	ausgabe[1] = ausgabe[1].split("t=")[1]
	# Newline am Ende abschneiden
	ausgabe[1] = ausgabe[1].rstrip()
	# 85000 ist ein Fehlercode
	if int(ausgabe[1]) == 85000:
		continue
	# Nur bei korrekter CRC ausgeben
	if ausgabe[0] == "YES\n":
		print ausgabe[1]
