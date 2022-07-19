import portage
import csv

p = portage.db[portage.root]["porttree"].dbapi
b_stats = dict()
stats = dict()
r_stats = dict()
all_packages = []

for type in ["BDEPEND", "DEPEND", "RDEPEND"]:
    for package in p.cp_all():
        for v in p.match(package):
            dependencies = p.aux_get(v, [type])[0].split('\n')
            all_packages += [package]
            if type == "DEPEND":
                stats[package] = dependencies
            if type == "BDEPEND":
                b_stats[package] = dependencies
            if type == "RDEPEND":
                r_stats[package] = dependencies

csv_columns = ['package', 'dependencies', 'b_dependencies', 'r_dependencies']

csv_file = "data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_columns)

        for package in all_packages:
            dep = stats[package]
            b_dep = b_stats[package]
            r_dep = r_stats[package]

            if dep == ['']:
                dep = ''
            if r_dep == ['']:
                r_dep = ''
            if b_dep == ['']:
                b_dep = ''
            writer.writerow([package, dep, b_dep, r_dep])
except IOError:
    print("I/O error")
