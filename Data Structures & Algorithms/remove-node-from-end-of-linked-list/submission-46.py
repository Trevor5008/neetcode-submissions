# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        
        prev, curr = None, head
        dist = length - n
        print(dist)
        while dist > 0:
            dist -= 1
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            return curr.next
        return head