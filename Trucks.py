import datetime
import Distances
import Interface
import Packages


def load_truck(packageID_list, hash_table, distance_list):
    truck_packages = []
    index_list = Packages.get_package_indexes(packageID_list, hash_table, distance_list)

    for package in packageID_list:
        my_package = hash_table.search(package)
        if my_package.package_id == 9:
            my_package.address = '410 S State St'

        truck_packages.append(my_package)
        # index_list.append(Distances.get_index(my_package.address, distance_list))
    for package in truck_packages:
        Distances.get_package_index(package, distance_list)
    # return truck_packages, index_list
    distances, used_indexes = Distances.nearest_neighbor(distance_list, index_list)
    return truck_packages, index_list, distances


class Trucks:
    package_list = []
    index_list = []
    distances = []
    total_distance = 0
    start_time = None

    def __init__(self, package_list, index_list, distances, start_time):
        self.package_list = package_list
        self.index_list = index_list
        self.distances = distances
        h, m, s = start_time.split(':')
        self.start_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        for package in self.package_list:
            package.status = "en route"

    def reset(self, packageID_list, hash_table, distance_list):

        for i, rows in enumerate(hash_table.table):
            for j, cols in enumerate(hash_table.table[i]):
                cols[1].status = 'en route'
        self.total_distance = 0
        truck_packages, truck_index_list, truck_distances = load_truck(packageID_list, hash_table, distance_list)
        self.package_list = truck_packages
        self.index_list = truck_index_list
        self.distances = truck_distances

        # for package in self.package_list:
        #     print(package.status)


    def full_deliver(self):  # TODO Add timestamp parameter
        # for package in self.package_list:
        #     print(f"BLARGH {package.package_id} {package.address_index}" )
        # for i in self.index_list:
        #     print(i)

        for i, distance in enumerate(self.distances):
            self.total_distance += distance
            delivering_index = self.index_list[i + 1]
            for package in self.package_list:

                if package.address_index == delivering_index:
                    package.status = "delivered"

        print(self.total_distance)

    def deliver(self, current_distance):
        i = 0

        while self.total_distance < current_distance:
            print("total distance vs current", self.total_distance, current_distance)
            self.total_distance += self.distances[i]
            delivering_index = self.index_list[i + 1]
            i += 1
            for package in self.package_list:
                if package.address_index == delivering_index and package.status != "Delivered":
                    elapsed_minutes = self.total_distance / .3
                    print(f"ELAPSED MINUTES {elapsed_minutes}")
                    h, m = Interface.get_time_delta(elapsed_minutes)
                    elapsed_delta = datetime.timedelta(hours=h, minutes=m)
                    package.status = "Delivered"
                    print(f"Delivering package {package.package_id} at {self.start_time + elapsed_delta}")
                    delivered_time = self.start_time + elapsed_delta
                    package.delivered_time = delivered_time
            if i >= len(self.distances):
                print("BREAKING OUT THIS BITCH!")
                break
            # if self.total_distance >= current_distance:
            #     break
        for package in self.package_list:
            print(package)
        print(f"TOTAL DISTANCE: {self.total_distance}")

    def list_packages(self):
        for package in self.package_list:
            print(package)
