# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        idx = 0
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        idx = length - n
        
        if idx == 0:
            return head.next

        curr = head
        while idx > 0:
            idx -= 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return head
        