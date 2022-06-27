import Packages
from HashTable import HashTable

ht1 = HashTable()

filename = 'PackageFile.csv'
Packages.read_load(filename, ht1)

mypack = ht1.search(14)
print(f"package number 14 address: {mypack.address}")
print(f"package id: {mypack.package_id}, deadline: {mypack.delivery_deadline}")

count = 1
for i in range(len(ht1.table)):
    for j in range(len(ht1.table[i])):
        mypack = ht1.search(count)
        count += 1
        print(f"package id {mypack.package_id}, {mypack.address} {mypack.city} {mypack.state} {mypack.zip_code}, "
              f"{mypack.delivery_deadline},{mypack.mass_kilo}, {mypack.special_notes} ")
print('Test change')