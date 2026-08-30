class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = [0]

        def dfs(r, c):
            if (
                not (0 <= r < rows and 0 <= c < cols) or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            area = 1
            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea[0] = max(maxArea[0], dfs(row, col))

        return maxArea[0]