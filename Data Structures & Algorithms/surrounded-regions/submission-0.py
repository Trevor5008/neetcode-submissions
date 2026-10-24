class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or board[r][c] != 'O'
            ):
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for row in range(rows):
            for col in range(cols):
                if (row in [0, rows - 1] or col in [0, cols - 1]) and board[row][col] == 'O':
                    dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
        return None