import csv


class Packages:

    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, mass_kilo, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.mass_kilo = mass_kilo
        self.special_notes = special_notes

    def __str__(self):
        # package = f"Package ID: {self.package_id}, Address: {self.address} {self.city}, {self.state} {self.zip_code}. " \
        #           f"Delivery Deadline {self.delivery_deadline} Mass: {self.mass_kilo}kg, " \
        #           f"Special Notes: {self.special_notes} "
        # return package
        return f"Package ID: {self.package_id}, Address: {self.address} {self.city}, {self.state} {self.zip_code}. " \
                  f"Delivery Deadline: {self.delivery_deadline} Mass: {self.mass_kilo}kg, " \
                  f"Special Notes: {self.special_notes} "


def read_load(filename, hash_table):
    with open(filename) as csvfile:
        my_reader = csv.reader(csvfile)
        for package in my_reader:
            # print(package[0])
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
            # my_package = Packages(package[0], package[1], package[2], package[3], package[4], package[5], package[6],
            #                       package[7])
            hash_table.insert(package_id, my_package)



