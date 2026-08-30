"""
Given an integer array 'nums' and integer 'k', return the 'k'
most frequent elements w/in the array
"""

from collections import Counter

class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        charCountMap = Counter(nums)
        res = sorted(charCountMap.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in res[:k]]