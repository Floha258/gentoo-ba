import matplotlib.pyplot as plt
import pandas as pd
import csv
from functools import reduce

x = []
y = []

r_deps = pd.read_csv("r_dependencies.csv", index_col=0)
r_deps = r_deps.sort_values(by=['#runtime_dependencies'])

deps = pd.read_csv("dependencies.csv", index_col=0)
deps = deps.sort_values(by=['#dependencies'])

b_deps = pd.read_csv("b_dependencies.csv", index_col=0)
b_deps = b_deps.sort_values(by=['#build_dependencies'])

p_deps = pd.read_csv("p_dependencies.csv", index_col=0)
p_deps = p_deps.sort_values(by=['#post_dependencies'])

list = [deps, b_deps, r_deps, p_deps]
all_deps = reduce(lambda left,right: pd.merge(left, right, on=["package"], how='outer'), list).fillna(0)

fig = all_deps.plot(label='Distribution of Dependencies', logy=False, legend=True, subplots=True)

# with open("r_dependencies.csv", "r") as csvfile:
#     reader = csv.reader(csvfile)
#     linecount = 0
#     for row in reader:
#         if linecount == 0:
#             linecount += 1
#             continue
#         x.append(row[0])
#         y.append(row[1])
#
# y.sort(key=int)

# plt.plot(x, y)
# plt.yticks(ticks=[0, 100, 200, 300, 400, 500, 1072, 1560], labels=['0', '100', '200', '300', '400', '500', '1072', '1560'])
plt.xticks([])
# fig.set_ylabel("Number of runtime dependencies")
plt.savefig("plot_r_dep.png")
