class HashTable:
    def __init__(self):
        self.data = {}

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def contains(self, key):
        return key in self.data

    def remove(self, key):
        if self.contains(key):
            del self.data[key]

    def keys(self):
        return list(self.data.keys())

    def values(self):
        return list(self.data.values())

    def clear(self):
        self.data = {}

    def size(self):
        return len(self.data)
