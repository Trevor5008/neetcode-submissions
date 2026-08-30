from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        res = []
        for key, v in counts.items():
            bucket[v].append(key)
        
        for i in reversed(range(len(bucket))):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res
        return res
