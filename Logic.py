class Logic:
    pass


def nearest_neighbor(positions_list):
    min_distance = 100.0
    for i in range(len(positions_list)):
        positions_list[i] = float(positions_list[i])
        if min_distance > positions_list[i] > 0.0:
            min_distance = positions_list[i]
            index = i
    del positions_list[index]

    return positions_list, index

