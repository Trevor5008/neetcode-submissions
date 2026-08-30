class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.index:
            node = self.index[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1       

    def put(self, key: int, value: int) -> None:
        if key in self.index:
            self._remove(self.index[key])
        node = ListNode(key, value)
        self.index[key] = node
        self._add(node)
        if len(self.index) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.index[lru.key]