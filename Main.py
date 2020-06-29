import pandas as pd
from Utils import distanceKM, Graph


nodes = list(range(1, 22))
myGraph = Graph(nodes)

for x in myGraph.nodes:
    for y in myGraph.nodes:
        if x != y:
            myGraph.add_edge(x, y, distanceKM(x, y))


edges = pd.DataFrame(myGraph.edges) #prettier and more readable output

print(edges)


