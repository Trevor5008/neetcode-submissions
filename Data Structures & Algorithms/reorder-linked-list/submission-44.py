# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        lst2 = slow.next
        prev = slow.next = None
        # reverse second half
        while lst2:
            tmp = lst2.next
            lst2.next = prev
            prev, lst2 = lst2, tmp
        # lst1 = 2 -> 4 -> 6 -> None
        # lst2 = 8 -> None
        lst1, lst2 = head, prev
        while lst2:
            tmp = lst1.next
            # tmp = None
            lst1.next = lst2
            # 2 -> 8
            lst1 = tmp
            # lst1 = 4 -> 6 -> None
            tmp2 = lst2.next
            # tmp2 = None
            lst2.next = lst1
            # 8 -> 4 -> 6 -> None 
            lst2 = tmp2
            # lst2 = None
        return None