from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lrows, lcols = len(board), len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(lrows):
            for col in range(lcols):
                val = board[row][col]
                if val == ".":
                    continue
                elif val in rows[row] or val in cols[col] or val in boxes[(row // 3, col // 3)]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                boxes[(row // 3, col // 3)].add(val)
        return True