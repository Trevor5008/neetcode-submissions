class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r, cols = 0, len(matrix)-1, len(matrix[0])-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols]:
                l, r = 0, cols
                while l <= r:
                    midc = (l + r) // 2
                    if matrix[mid][midc] == target:
                        return True
                    elif matrix[mid][midc] < target:
                        l = midc + 1
                    else:
                        r = midc - 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False