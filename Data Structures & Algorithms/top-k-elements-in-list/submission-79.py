class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        for val, idx in counts.items():
            buckets[idx].append(val)

        for lst in reversed(buckets):
            while lst and k > 0:
                res.append(lst.pop())
                k -= 1
            if k == 0:
                return res
        return []