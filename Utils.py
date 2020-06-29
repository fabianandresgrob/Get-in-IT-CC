import pandas as pd
import math
import numpy as np

raw_data = pd.read_csv('msg_standorte_deutschland.csv')

location_long_lat = raw_data[['msg Standort', 'Breitengrad', 'Längengrad']]
location_long_lat.index += 1


def distanceKM(locationX, locationY):
    """
    Calculating the great-circle-distance between two points by using the haversine formula.
    It returns the distance in km.
    """
    latitudeX = location_long_lat.iloc[locationX-1, 1]
    longitudeX = location_long_lat.iloc[locationX-1, 2]

    latitudeY = location_long_lat.iloc[locationY-1, 1]
    longitudeY = location_long_lat.iloc[locationY-1, 2]

    latitudeX, longitudeX, latitudeY, longitudeY = map(math.radians, [latitudeX, longitudeX, latitudeY, longitudeY])
    dlatitude = latitudeY - latitudeX
    dlongitude = longitudeY - longitudeX
    h = math.sin(dlatitude/2)**2 + math.cos(latitudeX) * math.cos(latitudeY) * math.sin(dlongitude/2)**2
    c = 2 * math.asin(math.sqrt(h))
    radius = 6371 #the radius of the earth in km
    return round(c*radius)


class Graph(object):

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = np.zeros((len(nodes), len(nodes)), dtype=int)

    def add_edge(self, sendingNode, receivingNode, weight):
        self.edges[sendingNode-1, receivingNode-1] =  weight #adjancecy matrix
        self.edges[receivingNode-1, sendingNode-1] =  weight #it really is an undirected graph, so it's symmetric

    def delete_edge(self, sendingNode, receivingNode):
        self.edges[sendingNode, receivingNode] = 0
        self.edges[receivingNode, sendingNode] = 0