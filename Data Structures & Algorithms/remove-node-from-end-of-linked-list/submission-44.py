# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, slow, fast = None, head, head
        
        while n > 0:
            fast = fast.next
            n -= 1

        if not fast:
            return head.next

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = prev.next.next
        return head