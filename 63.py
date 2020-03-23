class Solution:
    """
    TODO: 动态规划 -> 先求解子问题，在子问题的基础上求解总问题；
    TODO: 状态压缩 -> 将二维的路径求解问题压缩到一维，因为利用 for 循环的还每次处理一行；
    TODO：状态转移方程-> dp[j] = dp[j] + dp[j-1]
    TODO: 初始状态 -> dp = [1] + [0]*n
    """
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * m
        for i in range(n):
            for j in range(m):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j-1]

        # 因为数组 dp 多了一个元素
        return dp[-2]


res = Solution().uniquePathsWithObstacles([
    [0,0,0],
    [0,1,0],
    [0,0,0]
])
print(res)
