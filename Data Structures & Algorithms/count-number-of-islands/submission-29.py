class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        rows, cols = len(grid), len(grid[0])
        visited, q = set(), deque()
        islands = 0

        def bfs(r,c):
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
    
                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        (nr, nc) not in visited
                        and grid[nr][nc] == "1"
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands 