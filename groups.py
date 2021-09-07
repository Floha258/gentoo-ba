import csv

try:
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        sets = dict()
        all_rows = []
        for csvrow in reader:
            all_rows.append(csvrow)
        for row in all_rows:
            if line_count != 0:  # Ignore header
                set1 = set()
                if len(row) > 2:
                    for e in row[2:]:
                        set1.add(e)
                compare_count = line_count + 1  # we want to compare each row only once and not with itself
                for comparing_row in all_rows[compare_count:]:
                    if compare_count > line_count:
                        set2 = set()
                        if len(comparing_row) > 2:
                            for e in comparing_row[2:]:
                                set2.add(e)
                        set1 = frozenset(set1)
                        set2 = frozenset(set2)
                        # print(row[2:], comparing_row[2:])
                        # print(set1, set2)
                        intersection = set1 & set2
                        if len(intersection) != 0:  # don't add empty intersections
                            if intersection in sets:
                                sets[intersection] += 1
                            else:
                                sets[intersection] = 1
                    compare_count += 1
            line_count += 1

except IOError:
    print("data.csv file not found")


try:
    with open("groups.csv", "w") as groupsfile:
        writer = csv.writer(groupsfile)
        writer.writerow(["Occurrence of Group", "Groupflags"])
        for set, occurrence in sets.items():
            writer.writerow([occurrence, *set])

except IOError:
    print("Could not write file groups.csv")

