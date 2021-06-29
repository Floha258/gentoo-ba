import csv
import matplotlib.pyplot as plt
import pandas as pd
import math

start = 20
df = pd.read_csv('data.csv')

maxSize = 0

for package in df['#useflags']:
	if package > maxSize:
		maxSize = package
		print('Current Max Size: ' + str(maxSize))

bucketSize = math.floor(maxSize/(maxSize/25))  # make a bucket every 25
bucketAmount = math.ceil(maxSize/bucketSize)
buckets = [0] * bucketAmount
bucketLimits = [0] * bucketAmount
for i in range(bucketAmount):  # calculate the borders for the buckets
	bucketLimits[i] = (i + 1) * bucketSize
	if i == bucketAmount - 1:
		bucketLimits[i] = maxSize

print('Bucketlimits: ' + str(bucketLimits))

for package in df['#useflags']:  # count packages for buckets
	for i in range(bucketAmount):
		if bucketLimits[i] >= package >= start:
			buckets[i] += 1
			break

labels = [''] * bucketAmount

for i in range(bucketAmount):
	if i == 0:
		labels[i] = str(start) + ' - ' + str(bucketLimits[i])
	else:
		labels[i] = str(bucketLimits[i - 1] + 1) + ' - ' + str(bucketLimits[i])

print(buckets)
plt.pie(buckets, labels=labels)
plt.savefig("pie.jpg")
