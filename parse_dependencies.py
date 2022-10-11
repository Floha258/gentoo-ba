import csv

deps = dict()
b_deps = dict()
r_deps = dict()
p_deps = dict()

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    dict = dict()
    for row in reader:
        if line_count == 0:
            line_count += 1
            continue
        for (j, dep) in enumerate(row[1:]):
            string_to_parse = dep[2:-2]
            open_brackets = 0
            string_start = 0
            if row[0] == "x11-wm/wm2":
                print()
            for i, c in enumerate(string_to_parse):
                if c == '(':
                    open_brackets += 1
                if c == ')':
                    open_brackets -= 1
                if (c == ' ' and open_brackets == 0 and string_to_parse[i + 1] != '(') or (i == len(string_to_parse) - 1):

                    dependency = string_to_parse[string_start:i + 1]
                    string_start = i + 1
                    if j == 0:
                        if row[0] in deps.keys():
                            deps[row[0]] += [dependency.strip()]
                        else:
                            deps[row[0]] = [dependency.strip()]
                    if j == 1:
                        if row[0] in b_deps.keys():
                            b_deps[row[0]] += [dependency.strip()]
                        else:
                            b_deps[row[0]] = [dependency.strip()]
                    if j == 2:
                        if row[0] in r_deps.keys():
                            r_deps[row[0]] += [dependency.strip()]
                        else:
                            r_deps[row[0]] = [dependency.strip()]
                    if j == 3:
                        if row[0] in p_deps.keys():
                            p_deps[row[0]] += [dependency.strip()]
                        else:
                            p_deps[row[0]] = [dependency.strip()]
                else:
                    continue

with open("dependencies.csv", "w") as csvfile:
    csv_columns = ['package', '#dependencies', 'dependencies']
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for package, dependencies in deps.items():
        writer.writerow([package, len(dependencies), *dependencies])

with open("b_dependencies.csv", "w") as csvfile:
    csv_columns = ['package', '#build_dependencies', 'build_dependencies']
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for package, dependencies in b_deps.items():
        writer.writerow([package, len(dependencies), *dependencies])

with open("r_dependencies.csv", "w") as csvfile:
    csv_columns = ['package', '#runtime_dependencies']
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for package, dependencies in r_deps.items():
        writer.writerow([package, len(dependencies)])

with open("p_dependencies.csv", "w") as csvfile:
    csv_columns = ['package', '#post_dependencies', 'post_dependencies']
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for package, dependencies in p_deps.items():
        writer.writerow([package, len(dependencies), *dependencies])
