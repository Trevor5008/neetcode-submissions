# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        slow, fast = curr, curr

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        scnd = slow.next        
        prev = slow.next = None
        while scnd:
            tmp = scnd.next
            scnd.next = prev
            prev = scnd
            scnd = tmp

        frst, scnd = head, prev
        while scnd:
            tmp1, tmp2 = frst.next, scnd.next
            frst.next = scnd
            scnd.next = tmp1
            frst, scnd = tmp1, tmp2
