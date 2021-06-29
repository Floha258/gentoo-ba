import portage
import csv
import pandas as pd
import matplotlib.pyplot as plt

p = portage.db[portage.root]["porttree"].dbapi
a = "sys-apps/portage"
stats = dict()

for package in p.cp_all():
	for v in p.match(package):
		flags = p.aux_get(v, ["IUSE"])[0].split(' ')
		for flag in flags:
			if flag in stats:
				stats[flag] += 1
			else:
				stats[flag] = 1

bigDict = dict()
for key in stats.keys():
	val = stats[key]
	if 1200 <= val <= 1400 and key != '':
		bigDict[key] = val

x = bigDict.keys()
y = bigDict.values()
plt.bar(x, y)
plt.savefig("output.jpg")
