class HashMap:
    def __init__(self) -> None:
        self.HASH_TABLE_SIZE = 100
        self.hash_table = [[] for item in range(self.HASH_TABLE_SIZE)]

    def get_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)

        return hash_value % self.HASH_TABLE_SIZE

    def __setitem__(self, key, value):
        found = False

        index = self.get_hash(key=key)

        # Modify or update value at specified key if it exist
        for item_index, element in enumerate(self.hash_table[index]):
            if len(element) == 2 and element[0] == key:
                self.hash_table[index][item_index] = (key, value)
                found = True
                break

        # Insert value at specified key if it does not exist
        if not found:
            self.hash_table[index].append((key, value))

    def __getitem__(self, key):
        index = self.get_hash(key=key)

        for element in self.hash_table[index]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        index = self.get_hash(key=key)

        for item_index, element in enumerate(self.hash_table[index]):
            if element[0] == key:

                del self.hash_table[index][item_index]
