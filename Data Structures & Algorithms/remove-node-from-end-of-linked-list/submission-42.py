# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        while n > 0:
            fast = fast.next
            n -= 1

        if not fast:
            return head.next
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if prev:
            prev.next = prev.next.next
        return head