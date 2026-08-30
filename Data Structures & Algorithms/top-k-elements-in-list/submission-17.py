"""
Given an integer array 'nums' and integer 'k', return the 'k'
most frequent elements w/in the array
"""

from collections import Counter
import heapq

class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        charCountMap = Counter(nums)
        res = sorted(charCountMap.items(), key=lambda item: item[1], reverse=True)
        heap = [res[i][0] for i in range(len(res))]
        return heap[:k]