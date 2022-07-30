import csv
import Distances


class Packages:
    # Constructor
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, mass_kilo, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.mass_kilo = mass_kilo
        self.special_notes = special_notes
        self.address_index = None
        self.status = "at the hub"

    def __str__(self):
        return f"Package ID: {self.package_id}, Address: {self.address} {self.city}, {self.state} {self.zip_code}. " \
               f"Delivery Deadline: {self.delivery_deadline} Weight: {self.mass_kilo}kg Status: {self.status}"


# Iterates through packages CSV file and creates package objects from each row. It then inserts the package
# Objects into the main hash table. Called with a list of the delayed packages to set the status to delayed instead of
# at hub.
# O(n)
def read_load(filename, hash_table, delayed_packages):
    with open(filename) as csvfile:
        my_reader = csv.reader(csvfile)
        for package in my_reader:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            delivery_deadline = package[5]
            mass_kilo = package[6]
            special_notes = package[7]

            my_package = Packages(package_id, address, city, state, zip_code, delivery_deadline, mass_kilo,
                                  special_notes)

            if my_package.package_id in delayed_packages:
                my_package.status = 'Delayed'
            else:
                my_package.status = 'at hub'
            hash_table.insert(package_id, my_package)


# iterates through the list of packages (truck specific lists) and uses the distance table to return a list containing
# the address indexes of each package's delivery address.
def get_package_indexes(package_list, package_hash_table, distance_list):
    index_list = [1]
    for package in package_list:
        my_package = package_hash_table.search(package)
        index_list.append(Distances.get_index(my_package.address, distance_list))
    return index_list
