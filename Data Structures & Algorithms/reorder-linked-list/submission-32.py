# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        prev, lst2 = None, slow
        while lst2:
            tmp = lst2.next
            lst2.next = prev
            prev = lst2
            lst2 = tmp

        lst1, lst2 = head, prev
        while lst2.next:
            tmp1, tmp2 = lst1.next, lst2.next
            lst1.next, lst2.next = lst2, tmp1
            lst1, lst2 = tmp1, tmp2

        return None