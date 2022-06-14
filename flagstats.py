import csv

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

print("\nOn average a flag occurs in", totalFlags/len(flagsPerPackage), "packages")
print("On average a package has", totalPackages/len(packagesPerFlags), "flags\n")
print("Analysed", len(sortedPackages), "packages with", len(sortedFlags), "useflags")
