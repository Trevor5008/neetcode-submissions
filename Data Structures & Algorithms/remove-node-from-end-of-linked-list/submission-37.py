class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, slow, fast = None, head, head

        while fast and n > 0:
            fast = fast.next
            n -= 1
        
        if not fast: return head.next

        while slow and fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        prev.next = prev.next.next
        return head