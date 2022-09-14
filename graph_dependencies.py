import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("r_dependencies.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    linecount = 0
    for row in reader:
        if linecount == 0:
            linecount += 1
            continue
        x.append(row[0])
        y.append(row[1])

y.sort(key=int)

plt.plot(x, y)
plt.yticks(ticks=[0, 100, 200, 300, 400, 500, 1072, 1560], labels=['0', '100', '200', '300', '400', '500', '1072', '1560'])
plt.xticks([])
plt.savefig("barchart_r_dep.png")
