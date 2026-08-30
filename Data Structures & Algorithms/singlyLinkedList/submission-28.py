class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if not self.head: return -1
        curr = self.head 
        while curr:
            if index == 0:
                return curr.val 
            index -= 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        head = Node(val)
        head.next = self.head
        self.head = head 
        return

    def insertTail(self, val: int) -> None:
        tail = Node(val)
        if not self.head:
            self.head = tail
            return
        curr = self.head
        while curr and curr.next:
            curr = curr.next 
        curr.next = tail
        return

    def remove(self, index: int) -> bool:
        if not self.head: return False
        if index == 0:
            self.head = self.head.next
            return True
        prev, curr = None, self.head
        while curr:
            if index == 0:
                prev.next = curr.next
                return True
            index -= 1
            prev = curr
            curr = curr.next
        return False

    def getValues(self) -> List[int]:
        arr = []
        if not self.head:
            return arr
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr