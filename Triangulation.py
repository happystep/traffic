import numpy as np
import Parsing
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

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




# points = np.array([[0, 0], [0, 1], [0, 2], [8, 0], [1, 1], [1, 2],
#                         [3, 0], [0, 1], [2, 2]])
#vor = Voronoi(points)
#voronoi_plot_2d(vor)
#plt.show()
#
#vor = Voronoi(points)

print_points = np.array(all_sensorLatLong)

vor = Voronoi(print_points, incremental=True)

# Attributes of the voronoi diagram
#print(vor.points)
#print(vor.vertices)
#print(vor.ridge_points)
#print(vor.ridge_vertices)
#print(vor.regions)
#print(vor.point_region)

# testing adding a point to the existing plot
test = [[39, -95]]
point = np.array(test)


print("Voronoi Vertices")
print(vor.vertices)
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

first_region_location = vor.point_region[0]
first_region = vor.regions[first_region_location]

print(first_region_location)
print(first_region)

vertices_of_region = []

for x in first_region:
    vertices_of_region.append(vor.vertices[x])

print(vertices_of_region)
# for k, v in vor.ridge_dict:
#    print(k + v)
# voronoi_plot_2d(vor)
# plt.show()

# vor.add_points(point, restart=False)


plt.plot(point)
voronoi_plot_2d(vor)

# code for coloration of the polygons in the voronoi diagram
# for region in vor.regions:
#     if not -1 in region:
#         polygon = [vor.vertices[i] for i in region]
#         plt.fill(*zip(*polygon))

#save the vor cell regions, and then check against it by adding a new point with a method




plt.title("Voronoi I-35 North")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
