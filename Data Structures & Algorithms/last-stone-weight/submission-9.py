class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        two_heaviest = [-stone for stone in stones]
        heapq.heapify(two_heaviest)

        while len(two_heaviest) > 1:
            s1 = -heapq.heappop(two_heaviest)
            s2 = -heapq.heappop(two_heaviest)
            res = abs(s1-s2)
            if res > 0:
                heapq.heappush(two_heaviest, -abs(s1-s2))
        if len(two_heaviest) == 1:
            return -two_heaviest[0]
        else:
            return 0
        