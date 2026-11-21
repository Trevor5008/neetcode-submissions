class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            start = nums2.index(nums1[i])
            for j in range(start + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
            if len(res) < (i + 1): res.append(-1)
        return res