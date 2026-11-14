# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        heap = []
        heapq.heapify(heap)
        sent = ListNode()
        length = 0
        for lst in lists:
            curr = lst
            while curr:
                length += 1
                heapq.heappush(heap, curr.val)
                curr = curr.next
        curr = sent
        while length > 0:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
            length -= 1
        return sent.next