import graphviz
import csv
import itertools

graph = graphviz.Graph()
graphNodes = []
graphEdges = {}

try:
    with open("out2.csv", "r") as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                flags = row[2:]
                for flag1, flag2 in itertools.combinations(flags, 2):
                    if flag1 not in graphNodes:
                        graphNodes += [flag1]
                    if flag2 not in graphNodes:
                        graphNodes += [flag2]
                    if (flag1, flag2) not in graphEdges:
                        if (flag2, flag1) not in graphEdges:
                            # Can't make entirely sure which pair is actually stored so have to check for both pairs
                            graphEdges[(flag1, flag2)] = 1
                        else:
                            graphEdges[(flag2, flag1)] += 1
                    else:
                        graphEdges[(flag1, flag2)] += 1
            i += 1

except IOError:
    "could not open file out2.csv"

for node in graphNodes:
    graph.node(node)

for edge, weight in graphEdges.items():
    graph.edge(edge[0], edge[1], label=str(weight))

graph.save(filename="graph.gv")

print(graphNodes)
print(graphEdges)
