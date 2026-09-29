class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(max_heap)
        res = [-max_heap[0][0]]
        l, r = 0, k
        while r < len(nums):
            heapq.heappush(max_heap, (-nums[r], r))
            l += 1
            r += 1
            while max_heap[0][1] < l:
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])
        return res