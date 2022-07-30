import csv


# Reads through a csv file and creates a two-dimensional list containing business names and addresses in the first row
# and business names and columns in the first column. This first row and column should mirror each other. The cell
# matching the index of two different business represents the distance between each business, i.e.,
# distance_list[row][col] returns the distance between address at row and address at col
# O(n)
def read_load(filename):
    with open(filename) as csvfile:
        distance_list = list(csv.reader(csvfile, delimiter=','))

    return distance_list


# Uses the distance list to return the index of a specific business or address
# O(n)
def get_index(business_name, distance_list):
    distance_row = distance_list[0]
    for i in range(len(distance_row)):
        if business_name in distance_row[i]:
            return i


# Checks the package's address and then grabs the index of the address the package is to be delivered too
# O(1)
def get_package_index(package, distance_list):
    package.address_index = get_index(package.address, distance_list)


# This first row and column should mirror each other. The cell
# matching the index of two different business represents the distance between each business, i.e.,
# distance_list[row][col] returns the distance between address at row and address at col
# O(1)
def get_distance(x, y, distance_list):
    return distance_list[x][y]


# The nearest neighbor function first builds a list of duplicate indexes. This will be used later to deliver multiple
# packages that are going to the same address. It then orders the address indexes starting with the closest address to
# the WGU hub. It iterates through a row looking for the smallest distance. When it finds the smallest distance that
# belongs to an address in the list, it appends the distance to a distance list and moves to a new row matching the
# index of the address it just referenced. The distances list will be used later to keep track of the distance the
# truck is driving, and the used indexes will be referenced when delivering packages.
# O(n^3)
def nearest_neighbor(distance_list, indexes_list):
    duplicates = []
    used_duplicates = []

    # build duplicates list only of repeated elements. Only added when it is encountered after the first time.
    # Signifies multiple packages going to the same address.
    for num in indexes_list:
        if indexes_list.count(num) > 1 and num not in used_duplicates:
            repeat_times = indexes_list.count(num)
            used_duplicates.append(num)

            for i in range(repeat_times - 1):
                duplicates.append(num)

    min_distance = 100.0
    distances = []
    index = indexes_list[0]  # First element in the index list, should always be one, starting at WGU base
    used_indexes = [index]

    # Assigned to WGU's row, each index is the distance from WGU to the business in the matching column
    distance_row = distance_list[index]

    for i in range(len(indexes_list) - 1):
        for j in range(1, len(distance_row)):
            distance_row[j] = float(distance_row[j])
            if distance_row[j] < min_distance and (j != index or j in duplicates):
                if j in indexes_list and j not in used_indexes:
                    min_distance = distance_row[j]
                    index = j
                elif j in duplicates: # Multiple packages going to same address
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
