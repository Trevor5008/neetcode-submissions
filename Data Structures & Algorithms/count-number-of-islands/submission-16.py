from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        compass = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set((0,0))
        islands = 0
        
        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in compass:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols)
                    and grid[nr][nc] == '1' and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    bfs(r,c)
                    islands += 1
        return islands