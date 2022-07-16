import datetime
import Distances
import Interface
import Packages


# O(n^2)
def load_truck(packageID_list, hash_table, distance_list):
    index_list = Packages.get_package_indexes(packageID_list, hash_table, distance_list)
    for i, rows in enumerate(hash_table.table):
        for j, cols in enumerate(hash_table.table[i]):
            if cols[1].package_id in packageID_list:
                if cols[1].package_id == 9:
                    cols[1].address = '410 S State St'
            Distances.get_package_index(cols[1], distance_list)

    distances, used_indexes = Distances.nearest_neighbor(distance_list, index_list)
    return used_indexes, distances


class Trucks:
    package_list = []
    index_list = []
    distances = []
    total_distance = 0
    start_time = None
    end_time = None

    def __init__(self, packageID_list, index_list, distances, start_time, hash_table):
        self.package_list = packageID_list
        self.index_list = index_list
        self.distances = distances
        h, m, s = start_time.split(':')
        self.start_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        # for package in self.package_list:
        #     package.status = "en route"
        for i, rows in enumerate(hash_table.table):
            for j, cols in enumerate(hash_table.table[i]):
                if cols[1].package_id in packageID_list:
                    cols[1].status = 'en route'
    # O(1)
    def reset(self, packageID_list, hash_table, distance_list):

        self.total_distance = 0
        truck_index_list, truck_distances = load_truck(packageID_list, hash_table, distance_list)
        self.package_list = packageID_list
        self.index_list = truck_index_list
        self.distances = truck_distances
        self.end_time = None

    # O(n^2)
    def full_deliver(self, hash_table):

        for i, distance in enumerate(self.distances):
            self.total_distance += distance
            delivering_index = self.index_list[i + 1]

            for j, rows in enumerate(hash_table.table):
                for k, cols in enumerate(hash_table.table[j]):
                    if cols[1].package_id in self.package_list:
                        if cols[1].address_index == delivering_index and cols[1].status != 'delivered':
                            # cols[1].status = 'delivered'
                            delivered_time = convert_time(self.total_distance, self.start_time)
                            cols[1].status = f'Delivered at {delivered_time}.'

        self.end_time = convert_time(self.total_distance, self.start_time)

        # print(f"drove {self.distances[-1]} miles back to base. total_distance {self.total_distance} "
        #       f"Arrive at {self.end_time}")

    # O(n^2)
    def deliver(self, current_distance, current_time, hash_table):
        i = 0
        if current_time < self.start_time:
            return
        while self.total_distance < current_distance:
            self.total_distance += self.distances[i]
            delivering_index = self.index_list[i + 1]
            i += 1

            for j, rows in enumerate(hash_table.table):
                for k, cols in enumerate(hash_table.table[j]):
                    if cols[1].package_id in self.package_list:
                        if cols[1].address_index == delivering_index and cols[1].status != 'delivered':
                            # cols[1].status = 'delivered'
                            delivered_time = convert_time(self.total_distance, self.start_time)
                            cols[1].status = f'Delivered at {delivered_time}.'
                            if delivered_time >= current_time:
                                return

            if i >= len(self.distances):
                return

    def list_packages(self, hash_table):
        # for package in self.package_list:
        #     print(package)
        for i, rows in enumerate(hash_table.table):
            for j, cols in enumerate(hash_table.table[i]):
                if cols[1].package_id in self.package_list:
                    print(cols[1])

    # def display_package(self, package_id, hash_table):
    #     for j, rows in enumerate(hash_table.table):
    #         for k, cols in enumerate(hash_table.table[j]):
    #             if cols[1].package_id in self.package_list:
    #                 if cols[1].package_id == package_id:
    #                     print(cols[1])
    # for package in self.package_list:
    #     if package.package_id == package_id:
    #         print(package)


def convert_time(total_distance, start_time):
    elapsed_minutes = total_distance / .3
    h, m = Interface.get_time_delta(elapsed_minutes)
    elapsed_delta = datetime.timedelta(hours=h, minutes=m)
    delivered_time = start_time + elapsed_delta
    return delivered_time
