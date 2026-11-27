class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        stack = []
        for cur in nums2:
            while stack and cur > stack[-1]:
                nge[stack.pop()] = cur
            stack.append(cur)
        return [nge.get(v, -1) for v in nums1]