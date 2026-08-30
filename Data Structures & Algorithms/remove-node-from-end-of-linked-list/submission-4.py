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
        if n == 1 and length == 1:
            return
        prv, ptr = None, head
        while idx > 0:
            prv = ptr
            ptr = ptr.next
            idx -= 1
        if prv:
            prv.next = ptr.next
        else:
            return ptr.next
        return head
        