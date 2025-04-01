from sys import maxsize

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class ChainingHashTable:
    def __init__(self, max_size):
        self.table = [None] * max_size

    def hash(self, key) -> int:
        return abs(hash(key)) % len(self.table)

    def get(self, key):
        hash_idx = self.hash(key)

        if len(self.table) < hash_idx: 
            return None
        node = self.table[hash_idx]

        if not node:
            return None
    
        while node:
            if node.key == key:
                return node.value

            node = node.next

        return None
    
    def contains(self, key):
        hash_idx = self.hash(key)
        node = self.table[hash_idx]

        if not node:
            return False
    
        while node:
            if node.key == key:
                return True

            node = node.next

        return False

    def insert(self, key, value):
        hash_idx = self.hash(key)

        if not self.table[hash_idx]:
            self.table[hash_idx] = Node(key, value)
        elif self.contains(key):
            node = self.table[hash_idx]
            while node:
                if node.key == key:
                    node.value = value
                node = node.next
        else:
            head = self.table[hash_idx]
            new_head = Node(key, value)
            new_head.next = head
            self.table[hash_idx] = new_head

    def remove(self, key):
        hash_idx = self.hash(key)
        prev = None
        node = self.table[hash_idx]

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                    node = None
                else:
                    self.table[hash_idx] = None
                
                return

            prev = node
            node = node.next

    def get_keys(self):
        keys = []
        for i in range(len(self.table)):
            node = self.table[i] 
            while node:
                keys.append(node.key)
                node = node.next
        return keys
                
    def get_values(self):
        values = []

        for i in range(len(self.table)):
            node = self.table[i]
            while node:
                values.append(node.value)
                node = node.next

        return values
    
    
