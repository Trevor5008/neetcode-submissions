class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_bound, r_bound = 0, len(heights) - 1
        maxWater = 0
        while l_bound < r_bound:
            width = r_bound - l_bound
            currMax = min(heights[l_bound], heights[r_bound]) * width
            maxWater = max(maxWater, currMax)
            if heights[l_bound] < heights[r_bound]:
                l_bound += 1
            else:
                r_bound -= 1
        return maxWater