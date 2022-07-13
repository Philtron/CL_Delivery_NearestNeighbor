import Distances
import Packages
from HashTable import HashTable
from Trucks import Trucks, load_truck

ht1 = HashTable()


filename = 'Data/PackageFile.csv'
Packages.read_load(filename, ht1)

# for i, rows in enumerate(ht1.table):
#     for j, cols in enumerate(ht1.table[i]):
#         print(cols[1].address)

filename = "Data/DistanceTable2.csv"
distance_list = Distances.read_load(filename)

print('***')

# --------------------------
truck_packages = []
package_list = [3, 36, 38, 18, 1, 2, 4, 5, 7, 8, 29, 10, 17, 33, 35]
address_list = []
index_list = [1]
# for package in package_list:
#     my_package = ht1.search(package)
#     truck_packages.append(my_package)
#     address_list.append(my_package.address)
#     index_list.append(Distances.get_index(my_package.address, distance_list))
# # print(address_list)
#
# print(index_list)
# index_list = Packages.get_package_indexes(package_list, ht1, distance_list)
# ------------------------------
# for package in truck_packages:
#     Distances.get_package_index(package, distance_list)

truck_packages, index_list = load_truck(package_list, ht1, distance_list)
print(f'Line 40: {index_list}')

# for i, rows in enumerate(ht1.table):
#     for j, cols in enumerate(ht1.table[i]):
#         if cols[1].package_id in package_list:
#             print(cols[1].address_index)

distances, used_indexes = Distances.nearest_neighbor(distance_list, index_list)
print(f"distances: {distances}, used indexes: {used_indexes}")

# print(sum(distances))

truck1 = Trucks(truck_packages, index_list, distances)
truck1.list_packages()

truck1.deliver()
truck1.list_packages()
