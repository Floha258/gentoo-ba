import graphviz
import csv
import itertools

graph = graphviz.Graph(name='flag-relation', directory='graphviz-output')
graphNodes = []
graphEdges = {}
limit = 50

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

# for node in cleanedNodes:
#   graph.node(node)

# print('nodes added')

cleanedNodes = []

for edge, weight in graphEdges.items():
    if weight >= limit:
        if edge[0] not in cleanedNodes:
            graph.node(edge[0])
            cleanedNodes += [edge[0]]
        if edge[1] not in cleanedNodes:
            graph.node(edge[1])
            cleanedNodes += [edge[1]]
        graph.edge(edge[0], edge[1], label=str(weight))  # , label=str(weight)

print('edges added')

filename = f"graph_limit{limit}_labeled_cleaned.gv"
graph.save(filename=filename)
# graph.render(renderer='dot', filename='graph.png')
# graph.render(renderer='dot', outfile='graph.svg').replace('\\', '/')

# print(graphNodes)
# print(graphEdges)
