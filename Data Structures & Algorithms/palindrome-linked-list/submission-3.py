# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = deque()
        prev, curr = None, head
        while curr:
            q.append(curr.val)
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        while prev:
            curr = q.popleft()
            if prev.val != curr:
                return False
            prev = prev.next
        return True 