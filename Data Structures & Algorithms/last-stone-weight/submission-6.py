class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        stones.sort()
        while len(stones) > 1:
            stone1 = stones.pop()
            stone2 = stones.pop()
            diff = stone1 - stone2
            stones.append(diff)
            stones.sort()
        if len(stones) > 1:
            return stones[-1] - stones[-2]
        elif stones:
            return stones[-1]
        else:
            return 0
