class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr = lc = 0
        rr, rc = len(matrix)-1, len(matrix[0])-1
        while lr <= rr:
            mr = (lr + rr) // 2 
            if matrix[mr][0] <= target <= matrix[mr][rc]:
                while lc <= rc:
                    mc = (lc + rc) // 2
                    if matrix[mr][mc] == target:
                        return True
                    elif matrix[mr][mc] > target:
                        rc = mc - 1
                    else:
                        lc = mc + 1
            elif matrix[mr][0] > target:
                rr = mr - 1
            else:
                lr = mr + 1
        return False