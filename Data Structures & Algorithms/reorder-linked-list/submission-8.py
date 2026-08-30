class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # slow will stop at start of 2nd half of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        ptr = slow.next
        slow.next = None
        prev = None
        while ptr:
            tmp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = tmp
        
        curr = head
        while prev:
            tmp = curr.next
            curr.next = prev
            tmp2 = prev.next
            prev.next = tmp
            curr = tmp
            prev = tmp2