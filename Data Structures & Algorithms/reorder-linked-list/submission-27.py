# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev, slow, fast = None, head, head
        # Split halves using slow+fast ptrs
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        if prev: prev.next = None
        else: return
        # Reverse second half
        prev2 = None
        while slow:
            tmp = slow.next
            slow.next = prev2
            prev2 = slow
            slow = tmp

        # prev2 holds head of second half (reversed)
        curr = head
        while curr and prev2:
            tmp1 = curr.next
            curr.next = prev2
            curr = tmp1
            tmp2 = prev2.next
            if tmp1:
                prev2.next = tmp1
            prev2 = tmp2
        


