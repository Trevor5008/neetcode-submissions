class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0]) 
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                val = board[row][col]
                if val in row_set[row] or val in col_set[col] or val in box_set[(row // 3, col // 3)]:
                    return False
                if val == '.': continue
                row_set[row].add(val)
                col_set[col].add(val)
                box_set[(row // 3, col // 3)].add(val)
        return True