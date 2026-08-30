from collections import defaultdict

class Solution:
    # Input: 2D int array 'board'
    # Output: Bool (valid sudoku or not)
    # Each 3x3 subgrid must contain only unique 1-9 digits
    # Time O(n^2), Space O(n^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = defaultdict(set), defaultdict(set)
        grids = defaultdict(set)
        for row in range(9):
            for col in range(9):
                curr = board[row][col]
                if board[row][col] == '.':
                    continue
                # Value already used -> invalid
                elif (curr in rows[row] 
                    or curr in cols[col] 
                    or curr in grids[(row // 3, col // 3)]):
                        return False
                rows[row].add(curr)
                cols[col].add(curr)
                grids[(row // 3, col // 3)].add(curr)
        return True
        