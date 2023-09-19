class Node:
    def __init__(self, key, value):
        """linked list cell in form of:
        key -> value"""
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """It is important ot choose the right hash table size
    to maximize performance and reduce collisions"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key) -> int:
        """generate hash and take it modulo size,
        it fits in the table"""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """insert value in the table
        if linked list cell is None, initialize it and assign the value
        else if collision occurred, go to the end of the list and insert value"""
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        """Search for the value based on key
        if item is not found, KeyError is raised"""
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def remove(self, key):
        """Delete value from the table"""
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key):
        try:
            value = self.search(key)
            return value
        except KeyError:
            return "value does not exist"



if __name__ == '__main__':

    ht = HashTable(5)
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)
    print(ht['zxc'], 'zxc' in ht)