import Distances
import Packages
from HashTable import HashTable

ht1 = HashTable()

filename = 'Data/PackageFile.csv'
Packages.read_load(filename, ht1)

mypack = ht1.search(14)
print(f"package number 14 address: {mypack.address}")
print(f"package id: {mypack.package_id}, deadline: {mypack.delivery_deadline}")

count = 1
for i in range(len(ht1.table)):
    for j in range(len(ht1.table[i])):
        mypack = ht1.search(count)
        count += 1
        print(mypack)

ht2 = HashTable()
Distances.read_load('Data/DistanceTable.csv', 'Data/DistanceLocations.csv', ht2)
