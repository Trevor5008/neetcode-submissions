class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            currArea = (r - l) * min(heights[r], heights[l])
            maxArea = max(maxArea, currArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea