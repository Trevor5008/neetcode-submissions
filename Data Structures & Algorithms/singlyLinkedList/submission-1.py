class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        while curr and index >= 0:
            if index == 0:
                return curr.val
            curr = curr.next
            index -= 1
        return -1

    def insertHead(self, val: int) -> None:
        head = Node(val)
        head.next = self.head
        self.head = head
        return

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = Node(val)
        return

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        
        prev, curr = None, self.head
        while curr and index > 0:
            prev = curr
            curr = curr.next
            index -= 1
            
        if curr:
            prev.next = curr.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals