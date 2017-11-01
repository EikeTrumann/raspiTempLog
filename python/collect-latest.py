import os
import time

# Erzeugen eines relativen Pfades
logpath = os.path.join(os.path.join(os.path.dirname(__file__),os.pardir), 'logs')

outfile = open(logpath+"latest.txt", 'w')

# Konzept von Jan-Philip Gehrcke (stackoverflow)
# Findet alle csv-Dateien im logs-Verzeichnis
def csvSearch():
	for root, dirs, files in os.walk(path):
		for filename in files:
			if os.path.splitext(filename)[1] == ".csv":
				yield os.path.join(root, filename)

# Aus jeder Datei die letzte Zeile extrahieren
for csvfile in csvSearch():
	with open(csvfile) as file:
		for line in file:
			# Ueberspringt alle bis auf die letzte Zeile
			if not line.strip('\n'):
				continue
		# Tabellenzeile am Trennzeichen trennen
		contents = line.split(';')
		# Zeit aus Tabelle entnehmen
		lasttime = time.localtime(float(contents[0]))
		# Sensorname aus dem Dateinamen entnehmen
		sensorname = os.path.splitext(os.path.basename(csvfile))[0]
		# Sensorname und Zeit in Ausgabedatei schreiben
		outfile.write(sensorname.title() + " um " + time.strftime('%c',lasttime)+'\n')
		# Temperatur aus Tabelle in Ausgabedatei schreiben
		outfile.write("\t"+contents[1]+ " mC\n")
