class LinearProbingHashTable:

    def __init__(self, max_size, max_lf):
        self.keys = [None] * max_size
        self.values = [None] * max_size
        self.load = 0
        self.max_lf = max_lf

    def hash(self, key) -> int:
        return abs(hash(key)) % len(self.keys)

    def get(self, key):
        hash_idx = self.hash(key)

        while self.keys[hash_idx] != key:
            hash_idx = (hash_idx + 1) % len(self.keys)
        
        return self.values[hash_idx]

    def insert(self, key, value):
        if self.load / len(self.keys) >= self.max_lf:
            return

        self.load += 1
        hash_idx = self.hash(key)

        while self.keys[hash_idx] != None and self.keys[hash_idx] != key:
            hash_idx = (hash_idx + 1) % len(self.keys)

        self.keys[hash_idx] = key
        self.values[hash_idx] = value

    def remove(self, key):

        self.load -= 1

    def get_keys(self):
        return [key for key in self.keys if key]
    
    def get_values(self):
        return [value for value in self.values if value]