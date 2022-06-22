import csv
import numpy as np
from matplotlib import pyplot as plt

flagsPerPackage = dict()
packagesPerFlags = dict()

try:
    with open("out2.csv", "r") as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                flagsPerPackage[row[0]] = row[1]
                for flag in row[2:]:
                    if flag not in packagesPerFlags:
                        packagesPerFlags[flag] = 1
                    else:
                        packagesPerFlags[flag] += 1
            i += 1
except IOError:
    "could not open file out2.csv"

sortedFlags = sorted(packagesPerFlags.items(), key=lambda x: int(x[1]))
sortedPackages = sorted(flagsPerPackage.items(), key=lambda x: int(x[1]))

counter = 0
for package in sortedPackages:
    if package[1] > sortedPackages[0][1]:
        break
    else:
        counter += 1

print('Lowest Amount of flags per Package: ', sortedPackages[0][1], " flags found in ", counter, " packages\n")
top = 5
print('Top ', top, ' amount of flags per Package:')
for i in range(top):
    package = sortedPackages[len(sortedPackages) - top + i]
    print('#', top - i, ": ", package[0], " with ", package[1], " flags")

counter = 0

for flag in sortedFlags:
    if flag[1] > sortedFlags[0][1]:
        break
    else:
        counter += 1

print('\nLowest Amount of packages per Flag: ', sortedFlags[0][1], " packages found for ", counter, " flags\n")

print('Top ', top, ' amount of packages per Flag:')
for i in range(top):
    flag = sortedFlags[len(sortedFlags) - top + i]
    print('#', top - i, ": ", flag[0], " in ", flag[1], " packages")

totalFlags = 0
totalPackages = 0

for flag in sortedFlags:
    totalFlags += flag[1]

for package in sortedPackages:
    totalPackages += int(package[1])

print("\nOn average a flag occurs in", totalFlags / len(flagsPerPackage), "packages")
print("On average a package has", totalPackages / len(packagesPerFlags), "flags\n")
print("Analysed", len(sortedPackages), "packages with", len(sortedFlags), "useflags")


def gini(stats):
    n = len(stats)
    coef = 2.0 / n
    const = (1.0 + n) / n
    weighted_sum = 0
    for j, yj in enumerate(stats):
        weighted_sum += (j + i) * yj
    arrsum = 0
    for j in stats:
        arrsum += j
    return coef * weighted_sum / arrsum - const


arr = []

for p in sortedPackages:
    arr += [int(p[1])]

arr.sort()

print("Gini Coefficient: ", gini(arr))

X = np.array(arr)
X_lorenz = X.cumsum() / X.sum()
X_lorenz = np.insert(X_lorenz, 0, 0)

fig, ax = plt.subplots(figsize=[6, 6])
# scatter plot of Lorenz curve
ax.scatter(np.arange(X_lorenz.size) / (X_lorenz.size - 1), X_lorenz,
           marker='o', color='red', s=10)
# line plot of equality
ax.plot([0, 1], [0, 1], color='k')

plt.savefig("graphs/lorenzcurve.png")
