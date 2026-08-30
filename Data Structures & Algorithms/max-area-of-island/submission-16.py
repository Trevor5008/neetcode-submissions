class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        rows, cols = len(grid), len(grid[0])
        maxArea, q = 0, deque()
        
        def bfs(r, c):
            q.append((r, c))
            grid[r][c] = 0
            currArea = 1
            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        currArea += 1
            return currArea

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, bfs(row, col))
        
        return maxArea