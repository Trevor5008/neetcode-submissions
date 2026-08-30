# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at end of 1st half
        second = slow.next # second = start of 2nd half
        prev = slow.next = None # Detach second half
        # Reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # ptrs for start of each half
        first, second = head, prev
        # continue while 2nd half has nodes
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            first = tmp1
            second.next = first
            second = tmp2