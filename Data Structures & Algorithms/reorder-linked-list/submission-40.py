# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next: 
            prev =  slow
            slow = slow.next
            fast = fast.next.next

        # decouple 2nd list
        lst2 = slow.next
        slow.next = None
        prev = None
        while lst2:
            tmp = lst2.next
            lst2.next = prev
            prev = lst2
            lst2 = tmp
        
        # prev is now the head of the second half of the reversed list
        # start interleaving
        lst1, lst2 = head, prev
        while lst2:
            tmp1 = lst1.next
            tmp2 = lst2.next
            lst1.next = lst2
            lst2.next = tmp1
            lst1 = tmp1
            lst2 = tmp2

        return None