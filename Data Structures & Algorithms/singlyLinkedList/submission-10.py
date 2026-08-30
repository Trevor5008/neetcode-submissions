class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        while curr:
            if index == 0:
                return curr.val
            index -= 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) 
        new_node.next = self.head
        self.head = new_node
        return

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val) 
        return

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        
        curr = self.head
        while curr and curr.next:
            if index == 1:
                curr.next = curr.next.next
                return True
            curr = curr.next
            index -= 1

        return False

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

