import matplotlib.pyplot as plt
import pandas as pd
import numpy
import math
import csv
from scipy import interpolate

try:
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        dict = dict()
        for row in reader:
            if line_count != 0:
                if row[1] not in dict:
                    dict[row[1]] = 1
                else:
                    dict[row[1]] += 1
            line_count += 1

        sorted_keys = list(dict.keys())
        sorted_keys.sort(key=int)
        print(sorted_keys)
        dict2 = {}
        for i in sorted_keys:
            dict2[int(i)] = dict[i]
        dict = dict2
        print(dict)

except IOError:
    print("data.csv not found")

x = list(dict2.keys())
y = list(dict2.values())

###
# f1 = interpolate.interp1d(x, y, kind='linear')

# f2 = interpolate.interp1d(x, y, kind='cubic')

# plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.plot(x, y, 'o')
ax = plt.gca()
# ax.xaxis.set_tick_params(width=100)
# plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')
#plt.semilogy()
plt.savefig("plot.jpg")
