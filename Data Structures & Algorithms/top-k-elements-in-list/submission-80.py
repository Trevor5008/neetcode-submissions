class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, counts = [], Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for key, v in counts.items():
            buckets[v].append(key)

        for lst in reversed(buckets):
            while k > 0 and lst:
                res.append(lst.pop())
                k -= 1
        return res
