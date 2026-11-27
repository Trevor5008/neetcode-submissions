class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        valsMap = {v: i for i, v in enumerate(nums2)}
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            curr = nums1[i]
            for val, idx in valsMap.items():
                if val > curr and idx > valsMap[curr]:
                    res[i] = val
                    break
        return res