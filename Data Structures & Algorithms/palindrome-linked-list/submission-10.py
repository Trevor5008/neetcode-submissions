# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, lst2 = None, slow
        while lst2:
            tmp = lst2.next
            lst2.next = prev
            prev, lst2 = lst2, tmp

        while prev and head:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        return True