class HashTable:
    def __init__(self, table_size=10):
        self.table = []
        for i in range(table_size):
            self.table.append([])

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

    def search(self, key):
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            # print(f"kv[0] = {kv[0]}, key = {key}")
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        bucket = int(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
