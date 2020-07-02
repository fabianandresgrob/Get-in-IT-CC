import pandas as pd
import numpy as np
from Utils import distanceKM, Graph, findMin, travelingSalesman, get_names


nodes = list(range(21))
myGraph = Graph(nodes)

for x in myGraph.nodes:
    for y in myGraph.nodes:
        if x != y:
            myGraph.add_edge(x, y, distanceKM(x, y))


result = travelingSalesman(myGraph)


final_route = list(map(lambda x: x+1, result[0]))

get_names(result[0])
print('\n')
print(f'Finale Distanz: {result[1]} km')
print('\n')
print('Ausgabe in den Nummern: ', final_route)
