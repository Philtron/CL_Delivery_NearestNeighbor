import Distances
import Packages
from HashTable import HashTable
#
ht1 = HashTable()

filename = 'Data/PackageFile.csv'
Packages.read_load(filename, ht1)
#
mypack = ht1.search(14)
mypack2 = ht1.search(23)
# print(f"package number 14 address: {mypack.address}")
# print(f"package id: {mypack.package_id}, deadline: {mypack.delivery_deadline}")

# count = 1
# for i in range(len(ht1.table)):
#     for j in range(len(ht1.table[i])):
#         mypack = ht1.search(count)
#         count += 1
#         print(mypack)

ht2 = HashTable()
distance_list, distance_names = Distances.read_load('Data/DistanceTable.csv', 'Data/DistanceLocations.csv', ht2)
name1 = mypack.address
name2 = 'Western Governors University'

# for i in distance_names:
#     print(i)
row = Distances.get_index(name1, distance_names)
col = Distances.get_index(name2, distance_names)
print(f"Name: {distance_names[row]}")
print(f"Name: {distance_names[col]}")

print(f"Distance from {name1} to {name2} is {Distances.get_distance(row, col, distance_list)}")
