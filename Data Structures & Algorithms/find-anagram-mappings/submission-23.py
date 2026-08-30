class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numMap = {}
        for i in range(len(nums2)):
            numMap[nums2[i]] = i

        # {12: 0, 28: 0, 46: 0, 32: 0, 52: 0}

        for i in range(len(nums1)):
            nums1[i] = numMap[nums1[i]]

        return nums1