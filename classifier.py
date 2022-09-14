flags = []
classes = dict()

classes["unclassified"] = []
classes["python"] = []
classes["abi"] = []
classes["ruby"] = []
classes["databases"] = []
classes["documentation"] = []
classes["core_os"] = []
classes["dev_features"] = []
classes["x11"] = []

with open("./graphviz-output/graph_limit50_labeled_cleaned.gv") as graph:
    lines = graph.readlines()
    for line in lines[1:]:
        if ('--' in line) or ('}' in line):
            continue  # we do not care about edges currently
        if ("python" in line) or ("pip" in line):
            classes["python"].append(line.strip())
            continue
        if ('abi' in line):
            classes["abi"].append(line.strip())
            continue
        if ('ruby' in line):
            classes["ruby"].append(line.strip())
            continue
        if ('postgres' in line) or ('mysql' in line):
            classes["databases"].append(line.strip())
            continue
        if ('doc' in line) or ('handbook' in line):
            classes["documentation"].append(line.strip())
            continue
        if ('elibc' in line) or ('kernel' in line) or ('introspection' in line) or ("systemd" in line):
            classes["core_os"].append(line.strip())
            continue
        if ("debug" in line) or ('test' in line):
            classes["dev_features"].append(line.strip())
            continue
        if ("X" in line) or ("static-libs" in line):
            classes["x11"].append(line.strip())
            continue
        classes["unclassified"].append(line.strip())

print(classes)




