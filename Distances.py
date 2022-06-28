import csv


def read_load(filename, filename2, hash_table):
    # distance_names = {}
    with open(filename) as csvfile:
        distance_list = list(csv.reader(csvfile, delimiter=','))
    with open(filename2) as csvfile2:
        distance_names = list(csv.reader(csvfile2, delimiter=','))
        # my_reader = csv.reader(csvfile2)
        # for i, row in enumerate(my_reader):
        #     distance_names[i] = row[0]

    return distance_list, distance_names
    # for stuff in distance_list:
    #     print(stuff)
    #
    # for stuff in distance_names.values():
    #     print(stuff)
    #     print('__________________ ')
    #
    # print(distance_list[0][4])


def get_index(business_name, names_list):
    for i, business in enumerate(names_list):
        # print(f"Comparing {business_name} to {business}")
        for columns in business:
            if business_name in columns:
                return i
    return None


def get_distance(x, y, distance_list):
    return distance_list[x][y]


class Distances:
    pass
