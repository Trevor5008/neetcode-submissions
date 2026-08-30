class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        valueToPos = {nums2[i]: i for i in range(len(nums1))}

        mappings = [0] * len(nums1)
        for i in range(len(mappings)):
            mappings[i] = valueToPos[nums1[i]]

        return mappings