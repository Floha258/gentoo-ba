import csv
import enum

types = dict()
types_amount = dict()
types_amount["weakblocker"] = 0
types_amount["strongblocker"] = 0
types_amount["useconditional"] = 0
types_amount["anyofmany"] = 0
types_amount["slot"] = 0
types_amount["ranged"] = 0
types_amount["usedependant"] = 0
actual_constraints = dict()

with open("p_dependencies.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        if len(row) < 3:
            continue
        for dependency in row[2:]:
            type = ""
            for j, c in enumerate(dependency.strip()):
                if c == '!' and j == 0 and dependency[j + 1] != '!':
                    type = "weakblocker"
                    types_amount[type] += 1
                if c == '!' and j == 0 and dependency[j + 1] == '!':
                    type = "strongblocker"
                    types_amount[type] += 1
                if c == '?' and type == "":
                    type = "useconditional"
                    types_amount[type] += 1
                if c == '?' and type != "":
                    types_amount[type] -= 1
                    type = "useconditional"
                    types_amount[type] += 1
                if c == ':':
                    type = "slot"
                    types_amount[type] += 1
                if (c == '>' or c == '<' or c == '=' or c == '~') and (type != "ranged" or type != "slot" or type != "usedependant"):
                    type = "ranged"
                    types_amount[type] += 1
                if c == '[':
                    type = "usedependant"
                    types_amount[type] += 1
                if c == '|' and dependency[j + 1] == '|':
                    type = "anyofmany"
                    types_amount[type] += 1
            # types[dependency] = type
            # if dependency not in actual_constraints:
            #     actual_constraints[dependency] = 1
            # else:
            #     actual_constraints[dependency] += 1

# with open('stats_per_constraint.csv', 'w') as csvfile:
#     header = ["constraint", "occurrence", "type"]
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
#     for dependency, occurrence in actual_constraints.items():
#         writer.writerow([dependency, occurrence, types[dependency]])

with open('overall_dependency_stats.csv', 'w') as csvfile:
    header = ["type", "amount"]
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for type, amount in types_amount.items():
        writer.writerow([type, amount])
