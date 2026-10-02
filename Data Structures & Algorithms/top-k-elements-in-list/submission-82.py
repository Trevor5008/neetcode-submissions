class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, ct in count.items():
            heapq.heappush(heap, (ct, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [tup[1] for tup in heap]