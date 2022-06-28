import csv


def read_load(filename, filename2, hash_table):
    distance_names = {}
    with open(filename) as csvfile:
        distance_list = list(csv.reader(csvfile, delimiter=','))
    with open(filename2) as csvfile2:
        # distance_names = list(csv.reader(csvfile2))
        my_reader = csv.reader(csvfile2)
        for i, row in enumerate(my_reader):
            distance_names[i] = row[0]

    # for stuff in distance_list:
    #     print(stuff)

    for stuff in distance_names.values():
        print(stuff)


class Distances:
    pass
