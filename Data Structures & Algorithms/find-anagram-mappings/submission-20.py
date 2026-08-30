"""
Given two int arrays `nums1` and `nums2` where `nums2` is an anagram of `nums1`

return an index mapping array from nums1 -> nums2 where mapping[i] = j

Ex1: 1 = [12,28,46,32,50], 2 = [50,12,32,46,28] -> [1,4,3,2,0]
"""
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intMap = {}
        mappings = [0]*len(nums1)
        for i in range(len(nums2)):
            intMap[nums2[i]] = i
    
        for j in range(len(nums1)):
            mappings[j] = intMap[nums1[j]]

        print(mappings)
        return mappings
