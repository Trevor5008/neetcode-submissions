from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        # {1:1, 2:2: 3:3}
        # {7:2}
        freqs = [[] for _ in range(len(nums))]
        res = []
        for key, v in counts.items():
            freqs[v-1].append(key)
        print(freqs)
        for lst in reversed(freqs):
            while k > 0 and len(lst):
                res.append(lst.pop())
                k -= 1
        return res