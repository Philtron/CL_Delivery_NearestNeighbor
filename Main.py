import Distances
import Packages
from HashTable import HashTable
from Trucks import Trucks, load_truck

ht1 = HashTable()

filename = 'Data/PackageFile.csv'
Packages.read_load(filename, ht1)

filename = "Data/DistanceTable2.csv"
distance_list = Distances.read_load(filename)

print('***')
print("Truck One")
# --------------------------7   22  22  5   18  7   13  16  22  20  19  17
truck_one_packageID_list = [13, 15, 16, 19, 20, 39, 30, 31, 34, 37, 40, 12]
truck_one_packages, truck_one_index_list = load_truck(truck_one_packageID_list, ht1, distance_list)
print(f"Indexes List: {truck_one_index_list}")
truck_one_distances, used_indexes = Distances.nearest_neighbor(distance_list, truck_one_index_list)
truck_one = Trucks(truck_one_packages, truck_one_index_list, truck_one_distances)
truck_one.deliver()

print('-' * 100)
print("Truck Two")

truck_two_packageID_list = [3, 36, 38, 18, 1, 2, 4, 5, 7, 8, 29, 10, 17, 33, 35]
truck_two_packages, truck_two_index_list = load_truck(truck_two_packageID_list, ht1, distance_list)
truck_two_distances, used_indexes = Distances.nearest_neighbor(distance_list, truck_two_index_list)
print(f'Truck Two Indexes: {truck_two_index_list}')
truck_two = Trucks(truck_two_packages, truck_two_index_list, truck_two_distances)
truck_two.deliver()
print('-' * 100)
print("Truck Three")

truck_three_packageID_list = [6, 9, 25, 28, 32, 23, 11, 22, 26, 24, 21, 27, 14]
truck_three_packages, truck_three_index_list = load_truck(truck_three_packageID_list, ht1, distance_list)
truck_three_distances, used_indexes = Distances.nearest_neighbor(distance_list, truck_three_index_list)
print(f'Truck Two Indexes: {truck_three_index_list}')
truck_three = Trucks(truck_three_packages, truck_three_index_list, truck_three_distances)
truck_three.deliver()

print('-' * 100)
print("TEST TRUCK")
test_truck_packageID_list = [15, 16, 24]
test_truck_packages, test_truck_index_list = load_truck(test_truck_packageID_list, ht1, distance_list)
testTruck_distances, used_indexes1 = Distances.nearest_neighbor(distance_list, test_truck_index_list)
test_truck = Trucks(test_truck_packages, test_truck_index_list, testTruck_distances)
test_truck.list_packages()
test_truck.deliver()
# test_truck.list_packages()
# address_list = []
# index_list = [1]
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

# for i, rows in enumerate(ht1.table):
#     for j, cols in enumerate(ht1.table[i]):
#         if cols[1].package_id in package_list:
#             print(cols[1].address_index)

# for i, rows in enumerate(ht1.table):
#     for j, cols in enumerate(ht1.table[i]):
#         print(cols[1].address)
# duplicates = [2,3,5]
#
# for i in range(6):
#     if i in duplicates:
#         print(f"{i} is in duplicates")
