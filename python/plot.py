# This file can be used to plot the data for each single sensor.
# It outputs a pdf and a png plot for each sensor

# Die Importreihenfolge ist wichtig!
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Benennung der Sensoren (laut config-Datei)
names = []

# Konfigurationsdatei oeffnen
configfile = open("/home/pi/messungen/config/sensoren",'r')
config = configfile.readlines()
configfile.close()

# Auswerten der Konfigurationsdatei
for line in config:
        line = line.split(' ')
        names.append(line[0])

# Start der Messreihe aus config auslesen
# Dies ist der Zeitoffset gegenüber der 
startfile = open("/home/pi/messungen/config/start",'r')
start = float(startfile.readline())
startfile.close()
	
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
		values = line.split(';')
		# Wenn vor Startzeitpunkt: nicht eintragen
		if(float(values[0]) < float(start)):
			continue
		time.append(float(values[0]) - start)
		data.append(values[1])
	
	# Zeichnen
	plt.plot(time,data)
	plt.xlabel('Zeit ab Start [s]')
	plt.ylabel('Temperatur [mC]')
	plt.title(name.title())
	plt.grid(True)
	plt.savefig("/home/pi/messungen/plot/"+name+".png", format="png")
	plt.savefig("/home/pi/messungen/plot/"+name+".pdf", format="pdf")
	plt.cla()
