class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        lvl = 0
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col, lvl))

        while q:
            row, col, lvl = q.popleft()

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if (
                    nr in range(rows) and
                    nc in range(cols) and 
                    grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    q.append((nr, nc, lvl + 1))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return lvl