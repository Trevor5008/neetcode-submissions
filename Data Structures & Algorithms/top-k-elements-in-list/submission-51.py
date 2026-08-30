from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, v in countMap.items():
            buckets[v].append(key)
            
        while k > 0:
            for lst in reversed(buckets):
                for val in reversed(lst):
                    res.append(val)
                    if len(res) == k:
                        return res
        return res