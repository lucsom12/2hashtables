class QuadraticProbingHashTable:
    def __init__(self, max_size, max_lf):
        if max_size & (max_size - 1) != 0:  # if not a power of 2
            max_size = 1 << (max_size.bit_length())
        self.keys = [None] * max_size
        self.values = [None] * max_size
        self.load = 0
        self.max_lf = max_lf

    def hash(self, key) -> int:
        return abs(hash(key)) & (len(self.keys) - 1)
    
    def resize(self):
        old_keys = self.keys
        old_values = self.values
        # new_size = len(self.keys) * 2
        new_size = len(self.keys) * 2
        # Ensure the new size is a power of 2
        if new_size & (new_size - 1) != 0:  # if not a power of 2
            new_size = 1 << (new_size.bit_length())  # round up to the next power of 2
        self.keys = [None] * new_size
        self.values = [None] * new_size
        self.load = 0

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.insert(old_keys[i], old_values[i])  

    def contains(self, key):
        hash_idx = self.hash(key)
        start_idx = hash_idx  

        i = 1
        while self.keys[hash_idx] is not None:
            if self.keys[hash_idx] == key:
                return True
            hash_idx = (hash_idx + i*i) & (len(self.keys) - 1)
            i += 1
            if hash_idx == start_idx:  
                return False  

        return False

    def get(self, key):
        hash_idx = self.hash(key)
        start_idx = hash_idx

        i = 1
        while self.keys[hash_idx] is not None:
            if self.keys[hash_idx] == key:
                return self.values[hash_idx]
            hash_idx = (hash_idx + i*i) & (len(self.keys) - 1)
            i += 1
            if hash_idx == start_idx:  
                return None  
        
        return None

    def insert(self, key, value):        
        if self.load / len(self.keys) >= self.max_lf:
            self.resize()

        hash_idx = self.hash(key)

        i = 1
        while self.keys[hash_idx] is not None and self.keys[hash_idx] != key:
            hash_idx = (hash_idx + i*i) & (len(self.keys) - 1)
            i += 1

        if self.keys[hash_idx] is None:
            self.load += 1  

        self.keys[hash_idx] = key
        self.values[hash_idx] = value

    def remove(self, key):
        hash_idx = self.hash(key)
        start_idx = hash_idx

        i = 1
        while self.keys[hash_idx] is not None:
            if self.keys[hash_idx] == key:
                break
            hash_idx = (hash_idx + i*i) & (len(self.keys) - 1)
            i += 1
            if hash_idx == start_idx:  
                return  

        if self.keys[hash_idx] is None:
            return 
        
        self.keys[hash_idx] = None
        self.values[hash_idx] = None
        self.load -= 1  

        
        
        i = 1
        next_idx = (hash_idx + i*i) & (len(self.keys) - 1)
        while self.keys[next_idx] is not None:
            reinsert_key, reinsert_value = self.keys[next_idx], self.values[next_idx]
            self.keys[next_idx] = None
            self.values[next_idx] = None
            self.load -= 1  
            self.insert(reinsert_key, reinsert_value) 
            next_idx = (next_idx + i*i) & (len(self.keys) - 1)
            i += 1

    def get_keys(self):
        return [key for key in self.keys if key is not None]
    
    def get_values(self):
        return [value for value in self.values if value is not None]
