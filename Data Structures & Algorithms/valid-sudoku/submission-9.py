class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                curr = board[row][col]
                box = (row // 3, col // 3)
                if curr == '.': continue
                elif (
                    curr in rows[row] or
                    curr in cols[col] or 
                    curr in boxes[box]
                ):
                    return False
                rows[row].add(curr)
                cols[col].add(curr)
                boxes[(row//3,col//3)].add(curr)
        return True