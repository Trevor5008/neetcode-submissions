from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, v in countMap.items():
            buckets[v].append(key)
        for i in reversed(range(len(buckets))):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res