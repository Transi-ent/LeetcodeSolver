class Solution:
    def minPathSum(self, grid: list) -> int:
        if len(grid)==0:
            return 0
        if len(grid)==1:
            return sum([sum(ele) for ele in grid])

        dp = grid
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
                elif i==0 and j>0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j==0 and i>0:
                    # j==0
                    dp[i][j] = dp[i-1][j] + grid[i][j]
        print(grid)
        return dp[m-1][n-1]

res = Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(res)
