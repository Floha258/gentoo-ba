import csv

try:
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        sets = dict()
        for row in reader:
            if line_count != 0:
                compare_count = 0
                for comparing_row in reader:
                    # we want to compare each row only once and not with itself
                    if compare_count > line_count:
                        set1 = set()
                        set2 = set()
                        if len(row) >= 2:
                            for e in list(row[2:]):
                                print("Row: ", row[2:])
                                set1.add(e)
                        if len(comparing_row) >= 2:
                            for e in list(comparing_row[2:]):
                                set2.add(e)
                        set1 = frozenset(set1)
                        set2 = frozenset(set2)
                        #print(row[2], comparing_row[2])
                        #print(set1, set2)
                        intersection = set1 & set2
                        if intersection in sets:
                            sets[intersection] += 1
                        else:
                            sets[intersection] = 1
                    compare_count += 1
            line_count += 1

except IOError:
    print("data.csv file not found")
###
# for intersection, amount in dict.items():
#    print(intersection, " ", amount)
###
