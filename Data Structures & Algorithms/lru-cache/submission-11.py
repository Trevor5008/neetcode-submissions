class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def remove(self, node: Node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    # Insert node at right
    def insert(self, node):
        p, n = self.tail.prev, self.tail
        p.next = n.prev = node
        node.next, node.prev = n, p

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        
