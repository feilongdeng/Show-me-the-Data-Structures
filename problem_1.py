class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRU_Cache:
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.dict:
            self._remove(self.dict[key])
        node = Node(key, value)
        self._insert(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:

            node = self.head.next 

            self._remove(node)
            del self.dict[node.key]
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

#test 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))      # returns 1

print(our_cache.get(2))       # returns 2

print(our_cache.get(9))      # return -1 because it is nonexisten.

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


#test 2
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)

print(our_cache.get(1))      # should return 10

print(our_cache.get(2))      # should return 2


#test 3

our_cache = LRU_Cache(0)
our_cache.set(1, 1)

print(our_cache.get(1))      # should return -1
