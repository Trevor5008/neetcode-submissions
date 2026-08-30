from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0 
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        q, visited = deque(), set()
        maxArea = [0]

        def bfs(r, c):
            q.append((r,c))
            count = 1
            while q:
                row, col = q.popleft()
                visited.add((row, col))
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(rows) and nc in range(cols)
                        and grid[nr][nc] == 1 and (nr, nc) not in visited
                    ):
                        count += 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return count
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea[0] = max(bfs(row, col), maxArea[0])
        return maxArea[0]