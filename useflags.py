import portage
import pandas as pd
import matplotlib.pyplot as plt

p = portage.db[portage.root]["porttree"].dbapi
portage_versions = p.match("sys-apps/portage")
stats = dict()

for v in portage_versions:
    flags = p.aux_get(v, ["IUSE"])[0].split(' ')
    for flag in flags:
        if flag in stats:
            stats[flag] += 1
        else:
            stats[flag] = 1

useflags = pd.json_normalize(stats)
useflags.plot()


