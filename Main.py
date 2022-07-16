# WGUPS Routing Program
# Philip Sauer Student ID 001156531


import Distances
import Interface
import Packages
from HashTable import HashTable
from Trucks import Trucks, load_truck

ht1 = HashTable()
try:
    # O(n)
    filename = 'Data/PackageFile.csv'
    Packages.read_load(filename, ht1)
    # O(n)
    filename = "Data/DistanceTable2.csv"
    distance_list = Distances.read_load(filename)

    print('***')
    print("Truck One")
    truck_one_packageID_list = [13, 15, 16, 19, 20, 39, 30, 31, 34, 37, 40, 12, 1, 29, 14]
    # O(n^2)
    truck_one_index_list, truck_one_distances = load_truck(truck_one_packageID_list, ht1,
                                                           distance_list)
    print(f"Truck one index list {truck_one_index_list}")

    truck_one = Trucks(truck_one_packageID_list, truck_one_index_list, truck_one_distances, "08:00:00", ht1)
    # O(n^2)
    truck_one.full_deliver(ht1)
    print(f"Truck one start time {truck_one.start_time}")
    truck_one.list_packages(ht1)

    print('-' * 100)
    print("Truck Two")
    #
    truck_two_packageID_list = [3, 36, 38, 18, 2, 4, 5, 7, 8, 10, 17, 33, 35, 9]
    truck_two_index_list, truck_two_distances = load_truck(truck_two_packageID_list, ht1,
                                                           distance_list)
    truck_two = Trucks(truck_two_packageID_list, truck_two_index_list, truck_two_distances, "10:20:00", ht1)
    truck_two.full_deliver(ht1)
    print(f"Truck two start time: {truck_two.start_time}")
    truck_two.list_packages(ht1)

    print('-' * 100)
    print("Truck Three")
    truck_three_packageID_list = [6, 25, 28, 32, 23, 11, 22, 26, 24, 21, 27]
    truck_three_index_list, truck_three_distances = load_truck(truck_three_packageID_list, ht1,
                                                               distance_list)
    truck_three = Trucks(truck_three_packageID_list, truck_three_index_list, truck_three_distances, "09:05:00", ht1)
    truck_three.full_deliver(ht1)
    print(f"Truck three start time: {truck_three.start_time}")
    truck_three.list_packages(ht1)

    total_miles = truck_one.total_distance + truck_two.total_distance + truck_three.total_distance
    Interface.welcome_message(total_miles, truck_one, truck_two, truck_three, truck_one_packageID_list,
                              truck_two_packageID_list, truck_three_packageID_list, ht1, distance_list)

except FileNotFoundError:
    print('File not found')


