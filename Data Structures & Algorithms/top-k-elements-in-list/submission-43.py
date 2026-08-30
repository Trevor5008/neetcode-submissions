from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, counts = [], Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for key, v in counts.items():
            bucket[v].append(key)
        
        for i in reversed(range(len(bucket))):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                k -= 1
                if k == 0:
                    return res
        return res
