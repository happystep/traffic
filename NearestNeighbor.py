import numpy as np
from scipy.spatial import Voronoi, KDTree


class NearestNeighbor:
    def __init__(self, list_sensor_locations, k):
        self.sensor_location = np.array(list_sensor_locations)
        self.k = k

    def construct_voronoi(self):
        vor = Voronoi(self.sensor_location)
        return vor

    def construct_KDTREE(self):
        tree = KDTree(self.sensor_location)
        return tree

    def query_tree(self, k, query_point):
        tree = self.construct_KDTREE()
        result = tree.query(query_point, k=k)
        return result





