# WGUPS Routing Program
# Philip Sauer Student ID 001156531


import Distances
import Interface
import Packages
from HashTable import HashTable
from Trucks import Trucks, load_truck

# Main hash table to be used.
ht1 = HashTable()
try:
    # List to keep track of delayed packages.
    delayed_packages = [6, 25, 28, 32]
    filename = 'Data/PackageFile.csv'
    Packages.read_load(filename, ht1, delayed_packages)
    filename = "Data/DistanceTable2.csv"
    distance_list = Distances.read_load(filename)

    # This is the list of packages that will go on this truck.
    truck_one_packageID_list = [13, 15, 16, 19, 20, 39, 30, 31, 34, 37, 40, 12, 1, 29, 14]
    # Preparing the lists needed to create the truck object.
    truck_one_index_list, truck_one_distances = load_truck(truck_one_packageID_list, ht1,
                                                           distance_list)
    # Create Truck object.
    truck_one = Trucks(truck_one_packageID_list, truck_one_index_list, truck_one_distances, "08:00:00", ht1)
    # Run full delivery.
    truck_one.full_deliver(ht1)

    # This is the list of packages that will go on this truck.
    truck_two_packageID_list = [3, 36, 38, 18, 2, 4, 5, 7, 8, 10, 17, 33, 35, 9]
    # Preparing the lists needed to create the truck object.
    truck_two_index_list, truck_two_distances = load_truck(truck_two_packageID_list, ht1,
                                                           distance_list)
    # Create Truck object
    truck_two = Trucks(truck_two_packageID_list, truck_two_index_list, truck_two_distances, "10:20:00", ht1)
    # Run full delivery
    truck_two.full_deliver(ht1)

    # This is the list of packages that will go on this truck.
    truck_three_packageID_list = [6, 25, 28, 32, 23, 11, 22, 26, 24, 21, 27]
    # Preparing the lists needed to create the truck object.
    truck_three_index_list, truck_three_distances = load_truck(truck_three_packageID_list, ht1,
                                                               distance_list)
    # Create Truck Object
    truck_three = Trucks(truck_three_packageID_list, truck_three_index_list, truck_three_distances, "09:05:00", ht1)
    # Run full delivery
    truck_three.full_deliver(ht1)

    total_miles = truck_one.total_distance + truck_two.total_distance + truck_three.total_distance
    Interface.welcome_message(total_miles, truck_one, truck_two, truck_three, truck_one_packageID_list,
                              truck_two_packageID_list, truck_three_packageID_list, ht1, distance_list)

except FileNotFoundError:
    print('File not found')
