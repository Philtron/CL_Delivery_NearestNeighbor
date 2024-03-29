class HashTable:
    # Initialize has table with a default table size of 10
    def __init__(self, table_size=10):
        self.table = []
        for i in range(table_size):
            self.table.append([])

    # O(n)
    def insert(self, key, item):
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [int(key), item]
        bucket_list.append(key_value)
        return True

    # Takes the unique package ID as a parameter and returns a package object with the matching package ID
    # O(n)
    def search(self, key):
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # O(n)
    def remove(self, key):
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # O(n^2)
    def list_packages(self):
        for i, rows in enumerate(self.table):
            for j, cols in enumerate(self.table[i]):
                print(cols[1])

    # Resets hash table to default un delivered packages.
    # O(n^2)
    def reset_packages(self):
        delayed_packages = [6, 25, 28, 32]

        for i, rows in enumerate(self.table):
            for j, cols in enumerate(self.table[i]):
                if cols[1].package_id in delayed_packages:
                    cols[1].status = 'Delayed'
                else:
                    cols[1].status = 'At the hub'
                cols[1].delivered_time = 'Not Delivered'
