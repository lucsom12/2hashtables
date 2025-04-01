class LinearProbingHashTable:
    def __init__(self, max_size, max_lf):
        self.keys = [None] * max_size
        self.values = [None] * max_size
        self.load = 0
        self.max_lf = max_lf

    def hash(self, key) -> int:
        return abs(hash(key)) % len(self.keys)

    def resize(self):
        old_keys = self.keys
        old_values = self.values
        new_size = len(self.keys) * 2
        self.keys = [None] * new_size
        self.values = [None] * new_size
        self.load = 0

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.insert(old_keys[i], old_values[i])  

    def contains(self, key):
        hash_idx = self.hash(key)
        start_idx = hash_idx  

        while self.keys[hash_idx] is not None:
            if self.keys[hash_idx] == key:
                return True
            hash_idx = (hash_idx + 1) % len(self.keys)
            if hash_idx == start_idx:  
                return False  

        return False

    def get(self, key):
        hash_idx = self.hash(key)
        start_idx = hash_idx

        while self.keys[hash_idx] is not None:
            if self.keys[hash_idx] == key:
                return self.values[hash_idx]
            hash_idx = (hash_idx + 1) % len(self.keys)
            if hash_idx == start_idx:  
                return None  
        
        return None

    def insert(self, key, value):        
        while self.load / len(self.keys) >= self.max_lf:
            self.resize()

        hash_idx = self.hash(key)

        while self.keys[hash_idx] is not None and self.keys[hash_idx] != key:
            hash_idx = (hash_idx + 1) % len(self.keys)

        if self.keys[hash_idx] is None:
            self.load += 1  

        self.keys[hash_idx] = key
        self.values[hash_idx] = value

    def remove(self, key):
        hash_idx = self.hash(key)
        start_idx = hash_idx

        while self.keys[hash_idx] is not None:
            if self.keys[hash_idx] == key:
                break
            hash_idx = (hash_idx + 1) % len(self.keys)
            if hash_idx == start_idx:  
                return  

        if self.keys[hash_idx] is None:
            return 
        
        self.keys[hash_idx] = None
        self.values[hash_idx] = None
        self.load -= 1  

        
        next_idx = (hash_idx + 1) % len(self.keys)

        while self.keys[next_idx] is not None:
            reinsert_key, reinsert_value = self.keys[next_idx], self.values[next_idx]
            self.keys[next_idx] = None
            self.values[next_idx] = None
            self.load -= 1  
            self.insert(reinsert_key, reinsert_value) 
            next_idx = (next_idx + 1) % len(self.keys)

    def get_keys(self):
        return [key for key in self.keys if key is not None]
    
    def get_values(self):
        return [value for value in self.values if value is not None]
