"""
Given an integer array 'nums' and an integer 'k'
return the 'k' most frequent elements w/in the array

Ex1: [1,2,2,3,3,3], k = 2 -> [2,3]
Ex2: [7,7], k = 1 -> [1]
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) # {1: 1, 2: 2, 3: 3}
        stack = sorted(counts, key=lambda x: counts[x], reverse=True)
        return stack[:k]