import Distances
import Packages


def load_truck(packageID_list, hash_table, distance_list):
    truck_packages = []
    index_list = Packages.get_package_indexes(packageID_list, hash_table, distance_list)

    for package in packageID_list:
        my_package = hash_table.search(package)
        truck_packages.append(my_package)
        # index_list.append(Distances.get_index(my_package.address, distance_list))
    for package in truck_packages:
        Distances.get_package_index(package, distance_list)
    return truck_packages, index_list


class Trucks:
    package_list = []
    index_list = []
    distances = []
    total_distance = 0

    def __init__(self, package_list, index_list, distances):
        self.package_list = package_list
        self.index_list = index_list
        self.distances = distances
        for package in self.package_list:
            package.status = "en route"

    def deliver(self):  # TODO Add timestamp parameter
        for package in self.package_list:
            print(f"BLARGH {package.package_id} {package.address_index}" )
        for i in self.index_list:
            print(i)
        for i, distance in enumerate(self.distances):
            self.total_distance += distance
            delivering_index = self.index_list[i+1]
            # print(f'Self.index_list[i] = {self.index_list[i]}')
            for package in self.package_list:

                if package.address_index == delivering_index:
                    package.status = "delivered"
                    # print(f'Setting {package.package_id} to Delivered')
        print(self.total_distance)

    def list_packages(self):
        for package in self.package_list:
            print(package)
