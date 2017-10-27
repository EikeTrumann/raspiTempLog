# This script plots the data from all sensors into a single file

# Die Importreihenfolge ist wichtig!
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Benennung der Sensoren (laut config-Datei)
names = []

# Textstrings für den Plot
stringressources = {}

# Konfigurationsdatei oeffnen
configfile = open("/home/pi/messungen/config/sensoren",'r')
config = configfile.readlines()
configfile.close()

# Auswerten der Konfigurationsdatei
for line in config:
        line = line.split(' ')
        names.append(line[0])

# Strings aus configfile auslesen
with open("/home/pi/messungen/config/strings") as f:
    for line in f:
       (key, val) = line.split()
       d[int(key)] = val

# Start der Messreihe aus config auslesen
# startfile = open("/home/pi/messungen/config/start",'r')
# start = float(startfile.readline())
# startfile.close()

plt.figure(figsize=(32,16))
plot = plt.subplot(111)

for name in names:
	# Daten aus csv-Datei in der Arbeitsspeicher lesen
	csvfile = open("/home/pi/messungen/logs/"+name+".csv",'r')
	csv = csvfile.readlines()
	csvfile.close()

	# Listen fuer die zu speichernden Daten
	time = []
	data = []
	
	# Daten zeilenweise in Liste uebertragen
	for line in csv:
		values = line.split(',')
		# Wenn vor Startzeitpunkt: nicht eintragen
		#if(float(values[0]) < float(start):
		#	continue
		time.append(float(values[1]))
		data.append(values[2])
	
	# Zeichnen
	plot.plot(time, data, label=name.title())

# Beschriften und Ausgeben der Zeichnungen
box = plot.get_position()
plot.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=6)
plt.xlabel('Zeit ab Start [s]')
plt.ylabel('Temperatur [mC]')
plt.title("Temperatur bei Eike")
plt.grid(True)
plt.savefig("/home/pi/messungen/plot/"+"all"+".png", format="png")
plt.savefig("/home/pi/messungen/plot/"+"all"+".pdf", format="pdf")
