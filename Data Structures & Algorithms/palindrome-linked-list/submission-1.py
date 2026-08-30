# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, curr = None, head
        q = deque()
        while curr:
            q.append(curr.val)
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr1 = prev
        while curr1:
            val = q.popleft()
            if val != curr1.val:
                return False

            curr1 = curr1.next
        return True