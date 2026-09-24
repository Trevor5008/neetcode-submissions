class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r, cols = 0, len(matrix)-1, len(matrix[0])-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols]:
                lc, rc = 0, cols
                while lc <= rc:
                    midCol = (lc + rc) // 2
                    if matrix[mid][midCol] == target:
                        return True
                    elif matrix[mid][midCol] < target:
                        lc = midCol + 1
                    else:
                        rc = midCol - 1
                return False
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False