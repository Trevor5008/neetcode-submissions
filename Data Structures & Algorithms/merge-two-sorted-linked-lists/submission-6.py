class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        curr1, curr2 = list1, list2
        while curr1.next is not None and curr2 is not None:
            if curr2.val >= curr1.val and curr2.val < curr1.next.val:
                tmp = curr1.next
                curr1.next = curr2
                curr2 = tmp
            curr1 = curr1.next

        if curr2 is not None:
            curr1.next = curr2
            
        return list1