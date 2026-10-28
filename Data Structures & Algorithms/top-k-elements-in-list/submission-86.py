class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for ct, val in count.items():
            heapq.heappush(heap, (val, ct))
            if len(heap) > k:
                heapq.heappop(heap)
        return [val for ct, val in heap]