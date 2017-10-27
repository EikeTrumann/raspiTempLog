import time

# Namen und ID der Sensoren
names = []
keys = []

# Konfigurationsdatei oeffnen
configfile = open("/home/pi/messungen/config/sensoren",'r')
config = configfile.readlines()
configfile.close()

# Jede Konfigurationszeile ist ein Sensorname mit ID 
for line in config:
	line = line.split(' ')
	names.append(line[0])
	keys.append(line[1].rstrip())

# Ausgabedateien zum Anhaengen oeffnen
file = []
for i in range(len(names)):
	file.insert(i,open("/home/pi/messungen/logs/"+names[i]+".csv", 'a'))

# busy-loop zur schnellstmoeglichen Messdatenerfassung
start = time.time()
while 1:
	for i in range(len(names)):
		# Datei oeffnen
		ausgabe = open("/sys/bus/w1/devices/"+keys[i]+"/w1_slave").readlines()
		# Die ersten 10 Bloecke in der Datei sind die hexadezimalen Daten
		ausgabe[0] = ausgabe[0].split(' ')[11]
		# Hinter dem T steht die Temperatur
		ausgabe[1] = ausgabe[1].split("t=")[1]
		# Newline am Ende abschneiden
		ausgabe[1] = ausgabe[1].rstrip()
		# 85000 ist ein Fehlercode
		if int(ausgabe[1]) == 85000:
			continue
		if int(ausgabe[1]) == 127937:
                        continue
		# Nur bei korrekter CRC ausgeben
		if ausgabe[0] == "YES\n":
			file[i].write(str(time.time())+", "+str(time.time()-start)+", "+ausgabe[1]+",\n")
			file[i].flush()
