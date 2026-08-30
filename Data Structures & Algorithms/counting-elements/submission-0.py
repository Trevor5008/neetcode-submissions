class Solution:
    def countElements(self, arr: List[int]) -> int:
        vals = set(arr)
        count = 0
        for i in range(len(arr)):
            if arr[i] + 1 in vals:
                count += 1
        return count