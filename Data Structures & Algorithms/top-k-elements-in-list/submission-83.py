class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        counts = Counter(nums)
        res = []
        for key, val in counts.items():
            buckets[val].append(key)

        for lst in reversed(buckets):
            while lst and k > 0:
                res.append(lst.pop())
                k -= 1
        return res