import csv

with open('out2.csv','w') as out:
    writer = csv.writer(out)
    with open('data.csv') as f:
        reader = csv.reader(f)
        writer.writerow(next(reader))
        for row in reader:
            useflags = eval(row[2])
            writer.writerow([row[0], row[1], *useflags])