from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = Counter(nums)
        nums_map = dict(sorted(nums_map.items(), key=lambda item: item[1], reverse=True))
        return list(nums_map.keys())[:k]