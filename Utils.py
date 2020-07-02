import pandas as pd
import math
import numpy as np
from copy import deepcopy

raw_data = pd.read_csv('msg_standorte_deutschland.csv')

location_long_lat = raw_data[['msg Standort', 'Breitengrad', 'Längengrad']]


def distanceKM(locationX, locationY):
    """
    Calculating the great-circle-distance between two points by using the haversine formula.
    It returns the distance in km.
    """
    latitudeX = location_long_lat.iloc[locationX, 1]
    longitudeX = location_long_lat.iloc[locationX, 2]

    latitudeY = location_long_lat.iloc[locationY, 1]
    longitudeY = location_long_lat.iloc[locationY, 2]

    latitudeX, longitudeX, latitudeY, longitudeY = map(math.radians, [latitudeX, longitudeX, latitudeY, longitudeY])
    dlatitude = latitudeY - latitudeX
    dlongitude = longitudeY - longitudeX
    h = math.sin(dlatitude/2)**2 + math.cos(latitudeX) * math.cos(latitudeY) * math.sin(dlongitude/2)**2
    c = 2 * math.asin(math.sqrt(h))
    radius = 6371 #the radius of the earth in km
    return round(c*radius)

def findMin(list):
    minNotNull = 1000
    for x in list:
        if x < minNotNull and x != 0:
            minNotNull = x
    return minNotNull


def travelingSalesman(graph):
    g = deepcopy(graph) #making a copy of the graph, so it isn't a in-place operation.
    
    rest = g.nodes
    restEdges = g.edges
    currentnode = rest[0]
    route = [0]
    totalDis = 0
    rest.remove(currentnode)
    
    while rest:
        shorDis = findMin(restEdges[currentnode]) #find the nearest node
        totalDis += shorDis
        result = np.where(restEdges[currentnode] == shorDis) #getting the index of the nearest node
        shorDisInd = result[0][0] # np.where returns a tuple, so to extract the index this is needed
        route.append(shorDisInd) #appending the index, the next node, to our tour
        g.delete_all_edges(currentnode, rest) #delete all edges to this node as we visited this node
        currentnode = shorDisInd #setting the index of the nearest node as the currentnode to go on from there
        rest.remove(currentnode) #deleting it from the remaining nodes, also crucial for termination of loop
        
    route.append(0) #to go back to where we started
    totalDis = totalDis + distanceKM(currentnode, 0) #distance from the last node to the starting/ending point

    return (route, totalDis)

def get_names(nodes):
        for x in range(20):
            print(f'{location_long_lat.iloc[x, 0]:30} ---> \t{location_long_lat.iloc[x+1, 0]:15}')
        print(f'{location_long_lat.iloc[20, 0]:30} ---> \t{location_long_lat.iloc[0, 0]:15}')

    
class Graph(object):

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = np.zeros((len(nodes), len(nodes)), dtype=int)

    def add_edge(self, sendingNode, receivingNode, weight):
        self.edges[sendingNode, receivingNode] =  weight #adjancecy matrix
        self.edges[receivingNode, sendingNode] =  weight #it really is an undirected graph, so it's symmetric

    def delete_edge(self, sendingNode, receivingNode):
        self.edges[sendingNode, receivingNode] = 0
        self.edges[receivingNode, sendingNode] = 0
    
    def delete_all_edges(self, currentNode, nodes):
        for x in nodes:
            self.delete_edge(currentNode, x)
