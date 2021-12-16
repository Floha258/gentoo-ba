###
# Read all groups as sets
# Calculate the difference between two groups A, B as dif = len(A-B) + len (B - A)
# Do this for all groups
# For each group A, search the group with the lowest difference B, merge A + B (remove duplicates if needed)
# Remove Group B from the difference set
# Number of occurences A + B = # of occurences A + # of occurences B

import csv

csv_rows = []

try:
    with open("groups.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        for csvrow in reader:
            if line_count != 0:
                csv_rows.append(csvrow)
            line_count += 1

except IOError:
    print("file groups.csv not found")

all_groups = []

for row in csv_rows:
    occurrence = row[0]
    flags = set(row[1:])
    all_groups.append([flags, occurrence])

merged_groups = []

for i, group in enumerate(all_groups):
    diffs = []
    # don't need to check (A, B) and (B, A) and (A,A)
    for comparing_group in all_groups[i+1:]:
        # calculate the absolute difference as the sum of the elements of A/B and B/A
        diff = len((group[0] - comparing_group[0])) + len((comparing_group[0] - group[0]))
        diffs.append(diff)
        # this will error if it's the last group in the list
    if i != len(all_groups):
        ind = diffs.index(min(diffs))
        min_diff_group = all_groups[i + 1 + ind]
        merge = group[0].union(min_diff_group[0])
        merge_occurrence = group[1] + min_diff_group[1]
        merged_groups.append([merge, merge_occurrence, min(diffs)])

try:
    with open("refined_groups.csv", "w") as groupsfile:
        writer = csv.writer(groupsfile)
        writer.writerow(["Occurrence of Group", "Difference between old groups", "Groupflags"])
        for merge, merge_occurrence, group_diff in merged_groups:
            writer.writerow([merge_occurrence, group_diff, *merge])

except IOError:
    print("Could not write file groups.csv")



