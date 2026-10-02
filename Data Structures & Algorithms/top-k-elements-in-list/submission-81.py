class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        res = []
        for num, ct in counts.items():
            buckets[ct].append(num)
        
        for lst in reversed(buckets):
            while lst and k > 0:
                res.append(lst.pop())
                k -= 1
                if k == 0:
                    return res
        return []