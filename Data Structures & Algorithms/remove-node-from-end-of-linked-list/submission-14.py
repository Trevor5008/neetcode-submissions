class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        if n == 1 and not slow.next:
            return None
        count = n
        while fast and count > 0:
            fast = fast.next
            count -= 1

        if not fast:
            return head.next

        prev = slow
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        return head