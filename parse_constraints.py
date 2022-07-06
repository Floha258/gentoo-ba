import csv

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    dict = dict()
    for row in reader:
        if line_count == 0:
            line_count += 1
            continue
        if len(row) < 3:
            dict[row[0]] = []
            continue
        string_to_parse = row[2]
        open_brackets = 0
        string_start = 0
        for i, c in enumerate(string_to_parse):
            print(c)
            if c == '(':
                print("opening bracket")
                open_brackets += 1
            if c == ')':
                print("closing bracket")
                open_brackets -= 1
                if open_brackets == 0:
                    print("No open brackets")
                    constraint = string_to_parse[string_start:i + 1]
                    string_start = i + 1
                    if row[0] in dict.keys():
                        dict[row[0]] += [constraint.strip()]
                    else:
                        dict[row[0]] = [constraint.strip()]
            else:
                continue

with open("constraints.csv", "w") as csvfile:
    csv_columns = ['package', '#constraints', 'constraints']
    writer = csv.writer(csvfile)
    writer.writerow(csv_columns)
    for package, constraints in dict.items():
        writer.writerow([package, len(constraints), *constraints])
