import csv


def read_load(filename):
    with open(filename) as csvfile:
        distance_list = list(csv.reader(csvfile, delimiter=','))

    return distance_list


def get_index(business_name, distance_list):
    distance_row = distance_list[0]
    # print(f"Searching for {business_name}")
    # print(distance_row)
    index_list = []
    for i in range(len(distance_row)):
        if business_name in distance_row[i]:
            return i


def get_package_index(package, distance_list):
    package.address_index = get_index(package.address, distance_list)


def get_distance(x, y, distance_list):
    return distance_list[x][y]


def nearest_neighbor(distance_list, indexes_list):
    duplicates = {x for x in indexes_list if indexes_list.count(x) > 1}
    print(duplicates)

    min_distance = 100.0
    distances = []
    used_indexes = [indexes_list[0]]
    index = indexes_list[0]
    distance_row = distance_list[index]

    # 1 6 25 25 22 22

    for i in range(len(indexes_list) - 1):

        for j in range(1, len(distance_row)):

            distance_row[j] = float(distance_row[j])
            if min_distance > distance_row[j] and j != index:
                if j in indexes_list and j not in used_indexes:
                    min_distance = distance_row[j]
                    index = j
                elif j in duplicates:
                    min_distance = distance_row[j]
                    index = j
                    duplicates.remove(j)

        used_indexes.append(index)
        distances.append(min_distance)
        min_distance = 100.0
        distance_row = distance_list[index]

    return distances, used_indexes


class Distances:
    pass
