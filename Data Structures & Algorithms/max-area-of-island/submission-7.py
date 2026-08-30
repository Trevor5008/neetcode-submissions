class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = 1
                    q = deque([(r, c)])
                    visited.add((r, c))
                    while q:
                        row, col = q.popleft()
                        for dr, dc in dirs:
                            nr, nc = row + dr, col + dc
                            if (
                                nr in range(rows)
                                and nc in range(cols)
                                and grid[nr][nc] == 1 
                                and (nr, nc) not in visited
                            ):
                                currArea += 1
                                q.append((nr, nc))
                                visited.add((nr, nc))
                    maxArea = max(currArea, maxArea)
        
        return maxArea