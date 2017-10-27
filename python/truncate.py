import sys

print (sys.argv)

# Start der Messreihe aus config auslesen
path = sys.argv[1]
start = float(sys.argv[2])
stop = start + float(sys.argv[3])

print path
print start
print stop

# Benennung der Sensoren (laut config-Datei)
names = []

# Konfigurationsdatei oeffnen
configfile = open("./truncate.conf",'r')
config = configfile.readlines()
configfile.close()

# Auswerten der Konfigurationsdatei
for line in config:
        line = line.split(' ')
        out = line[0].rstrip()
        names.append(out)

for name in names:
    # Daten aus csv-Datei in der Arbeitsspeicher lesen
    csvfile = open(path+name+".csv",'r')
    csv = csvfile.readlines()
    csvfile.close()
    
    file = open(path+"/"+name+"-truncated.csv", 'w')
    
    # Daten zeilenweise in Liste uebertragen
    for line in csv:
        values = line.split(',')
        if(float(values[0]) < start):
            continue
        if(float(values[0]) > stop):
            continue
        file.write(str(float(values[0]) - start)+", "+values[1]+",\n")
    