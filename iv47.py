class Solution:
    def maxValue(self, grid: list) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return 0

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if not (i==0 and j==0):
                    if i==0:
                        grid[i][j] += grid[i][j-1]
                    elif j==0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += max(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
