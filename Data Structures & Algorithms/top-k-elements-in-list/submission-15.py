from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = Counter(nums)
        res = []
        # Sort the keys based on their frequency (counts) in descending order
        sorted_keys = sorted(numsCounter.keys(), key=lambda x: numsCounter[x], reverse=True)
        for key in sorted_keys:
            res.append(key)
        return res[:k]