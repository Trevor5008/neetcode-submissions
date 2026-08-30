from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqs = [[] for _ in range(len(nums))]
        res = []
        for key, v in counts.items():
            freqs[v-1].append(key)

        for lst in reversed(freqs):
            while k > 0 and len(lst):
                res.append(lst.pop())
                k -= 1
        return res