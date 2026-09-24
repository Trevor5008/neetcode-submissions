# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited, slow, fast = set(), head, head
        while fast and fast.next:
            if fast.val in visited:
                return True
            visited.add(slow.val)
            slow = slow.next
            fast = fast.next.next
        return False