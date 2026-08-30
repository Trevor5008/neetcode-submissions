from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        res = []
        for val in nums:
            countMap[val] = countMap.get(val, 0) + 1

        counts = [[] for _ in range(len(nums) + 1)]

        for key, val in countMap.items():
            counts[val].append(key)
        for lst in reversed(counts):
            while k > 0 and len(lst):
                res.append(lst.pop())
                k -= 1
        return res