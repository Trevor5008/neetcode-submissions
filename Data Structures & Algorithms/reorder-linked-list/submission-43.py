# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slw, fast = head, head
        while fast and fast.next:
            slw = slw.next
            fast = fast.next.next
        lst1, lst2 = head, slw.next  
        slw.next = None
        prev, curr = None, lst2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        lst2 = prev
        while lst1 and lst2:
            tmp1 = lst1.next
            lst1.next = lst2
            lst1 = tmp1
            tmp2 = lst2.next
            lst2.next = lst1
            lst2 = tmp2
        return None