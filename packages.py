import portage
import pandas as pd
import matplotlib.pyplot as plt
import csv

p = portage.db[portage.root]["porttree"].dbapi
stats = dict()

for package in p.cp_all():
	for v in p.match(package):
		flags = p.aux_get(v, ["IUSE"])[0].split(' ')
		stats[package] = flags

csv_columns = ['package', '#useflags', 'useflags']

csv_file = "data.csv"
try:
	with open(csv_file, 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(csv_columns)
		for package, flags in stats.items():
			writer.writerow([package, len(flags), flags])
except IOError:
	print("I/O error")
