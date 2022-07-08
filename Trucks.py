class Trucks:
    # package_list = []
    #
    # def __init__(self, package_list):
    #     self.package_list = package_list
    pass


# 5,4,11,10

def nearest_neighbor(distance_list, indexes_list):
    # indexes_list = [num - 1 for num in indexes_list]
    # del distance_list[0]
    min_distance = 100.0
    distances = []
    used_indexes = []
    index = indexes_list[0]
    distance_row = distance_list[index]
    # del distance_row[0]
    print(f"first distance print {distance_row}")

    for i in range(len(indexes_list)-1):
        used_indexes.append(index)  # last used index need to jump to this row

        for j in range(1, len(distance_row)):

            distance_row[j] = float(distance_row[j])
            if min_distance > distance_row[j] > 0.0:
                if j in indexes_list and j not in used_indexes:
                    min_distance = distance_row[j]
                    index = j

        distances.append(min_distance)
        min_distance = 100.0
        distance_row = distance_list[index]
        print(distance_row)
        # del distance_row[0]

    return distances, used_indexes
