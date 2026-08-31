class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        islands = 0
        
        def bfs(r,c):
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == "1"
                    ):
                        grid[nr][nc] = 0
                        q.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1
        return islands