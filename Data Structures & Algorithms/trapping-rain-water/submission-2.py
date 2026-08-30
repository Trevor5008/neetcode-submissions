class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = 0, 0
        heights, curr_vol = {}, 0

        for i in range(len(height)):
            if height[i] > max_l:
                max_l = height[i]
            heights[i] = max_l

        for i in reversed(range(len(height))):
            if height[i] > max_r:
                max_r = height[i]
            heights[i] = min(heights[i], max_r)
            curr_vol += heights[i] - height[i]
            curr_vol = curr_vol if curr_vol > 0 else 0
        return curr_vol