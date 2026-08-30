from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        for key, val in counts.items():
            buckets[val].append(key)

        for lst in reversed(buckets):
            while k > 0 and len(lst):
                res.append(lst.pop())
                k -= 1
        return res