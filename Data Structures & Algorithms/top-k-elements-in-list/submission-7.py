from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = Counter(nums)
        num_map = dict(sorted(num_map.items(), key=lambda item: item[1], reverse=True))
        return list(num_map.keys())[:k]
        