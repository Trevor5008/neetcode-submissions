class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        valueToPos = {}

        for i in range(len(nums2)):
            valueToPos[nums2[i]] = i

        mappings = [0] * len(nums1)
        for i in range(len(mappings)):
            mappings[i] = valueToPos[nums1[i]]

        return mappings