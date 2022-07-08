import Distances
import Trucks
import Packages
from HashTable import HashTable
import csv

#
ht1 = HashTable()

filename = 'Data/PackageFile.csv'
Packages.read_load(filename, ht1)

# for i, rows in enumerate(ht1.table):
#     for j, cols in enumerate(ht1.table[i]):
#         print(cols[1].address)

filename = "Data/DistanceTable2.csv"
distance_list = Distances.read_load(filename)

print('***')

# for i, business in enumerate(distance_list):
#     for j, columns in enumerate(business):
#         if '177 W Price Ave' in columns:
#             print(f'HI {i}, {j}')
#             x, y = i, j
#             break
#         if '2010 W 500 S' in columns:
#             y2, x2 = i, j
# (x, y, x2, y2) = Distances.get_index('177 W Price Ave', '2010 W 500 S', distance_list)
# print(f"x {x}, y {y}, x2 {x2}, y2 {y2}")
# print('***')
#
# distance_row = distance_list[1]
# del distance_row[0]
# print(distance_row)
#
#
# (distance_row, index, min_distance) = Trucks.nearest_neighbor(distance_row)
# print(f"Min Distance: {min_distance} Index: {index}")
#
# print(distance_row)
#
#
# (distance_row, index, min_distance) = Trucks.nearest_neighbor(distance_row)
# print(f"Min Distance: {min_distance} Index: {index}")
# print(distance_row)

indexes_list = [5, 4, 11, 10]
distances, used_indexes = Trucks.nearest_neighbor(distance_list, indexes_list)
print(f"distances: {distances}, used indexes: {used_indexes}")
