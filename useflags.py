import portage
import pandas as pd
import matplotlib.pyplot as plt

p = portage.db[portage.root]["porttree"].dbapi
a = "sys-apps/portage"
portage_versions = p.match(a)
print(portage_versions)
stats = dict()

#for package in p.cp_all():
for v in portage_versions:
    flags = p.aux_get(v, ["IUSE"])[0].split(' ')
    for flag in flags:
        if flag in stats:
            stats[flag] += 1
        else:
            stats[flag] = 1

print(stats)
x = stats.keys()
y = stats.values();
plt.bar(x, y)
plt.savefig("output.jpg")


