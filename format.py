import sys
import csv

site_names = []
lengths = []

with open("websites.txt", "rt") as file_name:
    for line in file_name:
        x = line.strip()
        site_names.append(x)

with open(sys.argv[1], "rt") as input_file:
    for line in input_file:
        x = line.strip()
        lengths.append(x)

with open('capture09.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['PacketLength', 'Website'])
    for i in range(0, len(site_names)):
        writer.writerow([lengths[i], site_names[i]])


