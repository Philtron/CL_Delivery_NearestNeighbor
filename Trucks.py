import datetime
import Distances
import Interface
import Packages


# builds the lists required to invoke the deliver and full deliver functions.  Gets the delivery address of each package
# and builds a list of indexes. Passes that list to the nearest neighbor function to build a list of distances from
# each index to the next. Also builds a new list containing the indexes in order or visitation, moving to the
# nearest qualifying index from the current index.
# O(n^3)
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


# Uses the calculated distance and the truck object's start time to determine exactly when a package would have been
# delivered.
# O(n)
def convert_time(total_distance, start_time):
    elapsed_minutes = total_distance / .3
    h, m = Interface.get_time_delta(elapsed_minutes)
    elapsed_delta = datetime.timedelta(hours=h, minutes=m)
    delivered_time = start_time + elapsed_delta
    return delivered_time


class Trucks:
    package_list = []
    index_list = []
    distances = []
    total_distance = 0
    start_time = None
    end_time = None

    # Constructor
    def __init__(self, packageID_list, index_list, distances, start_time, hash_table):
        self.package_list = packageID_list
        self.index_list = index_list
        self.distances = distances
        h, m, s = start_time.split(':')
        self.start_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        for i, rows in enumerate(hash_table.table):
            for j, cols in enumerate(hash_table.table[i]):
                if cols[1].package_id in packageID_list:
                    cols[1].status = 'en route'

    # resets the trucks fields back to default.
    # O(n^3)  due to the load_truck() function
    def reset(self, packageID_list, hash_table, distance_list):

        self.total_distance = 0
        truck_index_list, truck_distances = load_truck(packageID_list, hash_table, distance_list)
        self.package_list = packageID_list
        self.index_list = truck_index_list
        self.distances = truck_distances
        self.end_time = None

    # Uses the distance and used indexes list to simulate driving and delivering packages until the lists are empty
    # uses sums the distance list to determine total mileage and uses the total mileage and an eighteen mile per hour
    # speed to calculate total distance passed.
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

    # Uses the distance and used indexes list to simulate driving and delivering packages until it reaches the
    # calculated distance and time. This function is called by the user from the interface.
    # O(n^3)
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

    # lists the packages that the specific truck object has access too.
    # O(n^2)
    def list_packages(self, hash_table):
        for i, rows in enumerate(hash_table.table):
            for j, cols in enumerate(hash_table.table[i]):
                if cols[1].package_id in self.package_list:
                    print(cols[1])
