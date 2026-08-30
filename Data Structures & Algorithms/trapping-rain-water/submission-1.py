class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        vols = {}
        max_l, max_r = 0, 0
        for i in range(len(height)):
            max_l = max(height[i], max_l)
            vols[i] = max_l
        for i in reversed(range(len(height))):
            max_r = max(height[i], max_r)
            val = min(vols[i], max_r) - height[i]
            vols[i] = val if val >= 0 else 0
        print(vols)
        return sum(vols.values())

            