class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node):
        p, n = node.prev, node.next
        if p is not None:
            p.next = n
        if n is not None:
            n.prev = p

    def _add(self, node: Node):
        n = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = n
        n.prev = node

    def _pop_lru(self) -> Node:
        lru = self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
            return
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)

        if len(self.cache) > self.capacity:
            lru = self._pop_lru()
            del self.cache[lru.key]