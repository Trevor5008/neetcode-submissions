class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in counts.items():
            buckets[freq].append(val)

        res = []
        for lst in reversed(buckets):   
            while lst and k > 0:
                res.append(lst.pop())
                k -= 1
        return res