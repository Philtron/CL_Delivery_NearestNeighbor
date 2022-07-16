import csv


def read_load(filename):
    with open(filename) as csvfile:
        distance_list = list(csv.reader(csvfile, delimiter=','))

    return distance_list


def get_index(business_name, distance_list):
    distance_row = distance_list[0]
    for i in range(len(distance_row)):
        if business_name in distance_row[i]:
            return i


def get_package_index(package, distance_list):
    package.address_index = get_index(package.address, distance_list)


def get_distance(x, y, distance_list):
    return distance_list[x][y]


def nearest_neighbor(distance_list, indexes_list):
    duplicates = []
    used_duplicates = []

    for num in indexes_list:
        if indexes_list.count(num) > 1 and num not in used_duplicates:
            repeat_times = indexes_list.count(num)
            used_duplicates.append(num)

            for i in range(repeat_times - 1):
                duplicates.append(num)

    min_distance = 100.0
    distances = []
    index = indexes_list[0]
    used_indexes = [index]

    distance_row = distance_list[index]

    for i in range(len(indexes_list) - 1):
        for j in range(1, len(distance_row)):
            distance_row[j] = float(distance_row[j])
            if distance_row[j] < min_distance and (j != index or j in duplicates):
                if j in indexes_list and j not in used_indexes:
                    min_distance = distance_row[j]
                    index = j
                elif j in duplicates:
                    min_distance = 0
                    index = j
                    duplicates.remove(j)
        used_indexes.append(index)
        distances.append(min_distance)
        min_distance = 100.0
        distance_row = distance_list[index]
    drive_home = distance_list[1][index]
    distances.append(drive_home)
    used_indexes.append(1)
    return distances, used_indexes


class Distances:
    pass
