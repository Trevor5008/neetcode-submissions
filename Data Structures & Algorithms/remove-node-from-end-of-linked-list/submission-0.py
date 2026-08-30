class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        move = length - n
        if move == 0:
            return head.next
        
        curr = head
        while move > 0:
            move -= 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return head