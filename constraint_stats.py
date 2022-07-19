import csv
import enum

types = dict()
types_amount = dict()
types_amount["implications"] = 0
types_amount["oneof"] = 0
types_amount["atleastoneof"] = 0
types_amount["implicationoneof"] = 0
types_amount["maxoneof"] = 0
actual_constraints = dict()

with open("constraints.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        if len(row) < 3:
            continue
        for constraint in row[2:]:
            type = ""
            for j, c in enumerate(constraint):
                if c == '?' and constraint[j + 1] != '?' and type == "":
                    type = "implications"
                    types_amount[type] += 1
                if c == '^' and constraint[j + 1] == '^':
                    type = "oneof"
                    types_amount[type] += 1
                if c == '|' and constraint[j + 1] == '|' and type == "":
                    type = "atleastoneof"
                    types_amount[type] += 1
                if c == '|' and constraint[j + 1] == '|' and type == "implications":
                    type = "implicationoneof"
                    types_amount["implications"] = types_amount["implications"] - 1
                    types_amount[type] += 1
                if c == '?' and constraint[j + 1] == '?':
                    type = "maxoneof"
                    types_amount["maxoneof"] += 1
            types[constraint] = type
            if constraint not in actual_constraints:
                actual_constraints[constraint] = 1
            else:
                actual_constraints[constraint] += 1

with open('stats_per_constraint.csv', 'w') as csvfile:
    header = ["constraint", "occurrence", "type"]
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for constraint, occurrence in actual_constraints.items():
        writer.writerow([constraint, occurrence, types[constraint]])

with open('overall_constraint_stats.csv', 'w') as csvfile:
    header = ["type", "amount"]
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for type, amount in types_amount.items():
        writer.writerow([type, amount])
