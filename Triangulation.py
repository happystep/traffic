import numpy as np
import Parsing
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
from scipy.spatial import  KDTree, tsearch


data = Parsing.parse("individual_sensors_data.csv")
# print(data)

long = []
lat = []

cur = []

for y in data:
    for k, v in y.items():
        if v == "I35 N":
            cur.append(y)

for x in cur:
    for k, v in x.items():
        if k == "Longitude":
            long.append(float(v))
        elif k == "Latitude":
            lat.append(float(v))
# print(lat)
# print(long)



all_sensorLatLong = []

for x in range(0, len(lat)-1):
    one_sensor_list = []
    one_sensor_list.append (lat[x])
    one_sensor_list.append (long[x])
    all_sensorLatLong.append(one_sensor_list)


print_points = np.array(all_sensorLatLong)

# an attempt of querying based of the KDTree that can be taken from the initial points?

vor = Voronoi(print_points, incremental=True)

print("KD Tree based on Voronoi Vertices")
tree = KDTree(vor.vertices)
#
print("Test of KDTree query")
#test of tree
print(tree.query([39, -95], k=3))
print(tree.query([39, -95])[1])


point_tree = tree.query([39, -95], k=3)[1]
print("point containing test point")
print(point_tree)

print("Tree Data")
print(tree.data[point_tree])
print(len(tree.data))



print("KD Tree based on sensor locations")
tree = KDTree(print_points)

print("Test of KDTree query")
#test of tree
print(tree.query([39, -95],k=3))
print(tree.query([39, -95])[1])


point_tree = tree.query([39, -95],k=3)[1]
print("point containing test point")
print(point_tree)



print("Tree Data")
print(tree.data[point_tree])
print(len(tree.data))







print("Voronoi Vertices")
print(vor.vertices)
print(len(vor.vertices))
print(" ")
print("Voronoi Regions")
print(vor.regions)
print(" ")
print("Voronoi Point Region")
print(vor.point_region)
print(" ")
print("Points")
print(vor.points)
print(len(vor.point_region))
print("Voronoi Ridges")
print(vor.ridge_vertices)
print("Voronoi Ridge Points")
print(vor.ridge_points)
print("Voronoi Ridge Dict")
print(vor.ridge_dict)


#voronoi_plot_2d(vor)

# code for coloration of the polygons in the voronoi diagram
# for region in vor.regions:
#     if not -1 in region:
#         polygon = [vor.vertices[i] for i in region]
#         plt.fill(*zip(*polygon))

#save the vor cell regions, and then check against it by adding a new point with a method




#plt.title("Voronoi I-35 North")
#plt.xlabel("Longitude")
#plt.ylabel("Latitude")
#plt.show()
