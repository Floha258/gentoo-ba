import portage
import csv

p = portage.db[portage.root]["porttree"].dbapi
stats = dict()

for package in p.cp_all():
    for v in p.match(package):
        flags = p.aux_get(v, ["REQUIRED_USE"])[0].split('\n')
        stats[package] = flags

csv_columns = ['package', '#constraints', 'constraints']

csv_file = "data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_columns)
        for package, flags in stats.items():
            clean_flags = list(set(flags))
            if clean_flags == ['']:
                clean_flags = []
            writer.writerow([package, len(clean_flags), *clean_flags])
except IOError:
    print("I/O error")
