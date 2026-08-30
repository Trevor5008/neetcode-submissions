"""
Given an integer array 'nums' and an integer 'k'
return the 'k' most frequent elements w/in the array

Ex1: [1,2,2,3,3,3], k = 2 -> [2,3]
Ex2: [7,7], k = 1 -> [1]
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res