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
    # duplicates = {x for x in indexes_list if indexes_list.count(x) > 1}
    # print(duplicates)
    # for i in range(len(duplicates)):
    duplicates = []
    used_duplicates = []
    # for i in range(len(indexes_list)-1):
    #     for j in range(i+1, len(indexes_list)):
    #         if int(indexes_list[i]) == int(indexes_list[j]):
    #             duplicates.append(indexes_list[i])
    # print(f"indexes: {indexes_list}")
    for num in indexes_list:
        if indexes_list.count(num) > 1 and num not in used_duplicates:
            repeat_times = indexes_list.count(num)
            used_duplicates.append(num)
            for i in range(repeat_times):
                duplicates.append(num)
    print(f"duplicates: {duplicates}")

    min_distance = 100.0
    distances = []
    used_indexes = [indexes_list[0]]
    index = indexes_list[0]
    distance_row = distance_list[index]

    # 1 6 25 25 22 22

    for i in range(len(indexes_list) - 1):

        for j in range(1, len(distance_row)):

            distance_row[j] = float(distance_row[j])
            # print(f"min distance:{min_distance} index: {index} duplicates {duplicates}")

            if min_distance > distance_row[j] and (j != index or j in duplicates):
                # print(f"{j} in {duplicates}? {j in duplicates}")
                if j in indexes_list and j not in used_indexes:
                    min_distance = distance_row[j]
                    index = j
                elif j in duplicates:
                    min_distance = 0
                    index = j
                    duplicates.remove(j)
                # print(f'duplicates after removal {duplicates}')
        used_indexes.append(index)  # 23 22 22
        distances.append(min_distance)  # 2.4 4.4
        min_distance = 100.0
        distance_row = distance_list[index]

    print(f"Used Indexes: {used_indexes}")
    print(f"Distances: {distances} Total: {sum(distances)}")
    return distances, used_indexes


class Distances:
    pass
