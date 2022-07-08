import csv


def read_load(filename):
    with open(filename) as csvfile:
        distance_list = list(csv.reader(csvfile, delimiter=','))

    return distance_list


def get_index(business_name, business_name2, names_list):
    for i, business in enumerate(names_list):
        for j, columns in enumerate(business):
            if business_name in columns:
                x, y = i, j
            if business_name2 in columns:
                y2, x2 = i, j
    return (x, y, x2, y2)


def get_distance(x, y, distance_list):
    return distance_list[x][y]


class Distances:
    pass
