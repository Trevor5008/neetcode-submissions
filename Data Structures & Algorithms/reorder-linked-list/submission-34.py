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
        
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        lst1, lst2 = head, prev
        while lst2:
            tmp1, tmp2 = lst1.next, lst2.next
            lst1.next = lst2
            lst2.next = tmp1
            lst1, lst2 = tmp1, tmp2
        return