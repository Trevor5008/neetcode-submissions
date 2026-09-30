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

        prev = None
        lst2 = slow
        while slow:
            tmp = slow.next
            slow.next = prev
            prev, slow = slow, tmp

        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True