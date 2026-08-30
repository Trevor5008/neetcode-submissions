"""
Given two integer arrays: nums1, nums2
where nums2 is an anagram of nums1 (both arrays may contain duplicates)
Return an index mapping array "mapping" from nums1 to nums2 where mapping[i] = j

Ex. nums1 = [12, 28, 46, 32, 50], nums2 = [50, 12, 32, 46, 28] 
=> [1,4,3,2,0]
"""
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapped = {v: k for k, v in enumerate(nums2)}
        mapping = [0]*len(nums1)
        for i in range(len(nums1)):
            mapping[i] = mapped[nums1[i]]
        return mapping
            