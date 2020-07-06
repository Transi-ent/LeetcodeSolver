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

class Solution2:
    """
    动态规划：dp[i][j]表示从(1, 1)点到(i, j)有多少种不同的路径
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    """
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1] = 1 ## 从起点到该点本身只有1条路
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i+1][j+1] = 0
                else:
                    if i == 0 and j == 0:
                        continue
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        print(dp)
        return dp[m][n]


res = Solution2().uniquePathsWithObstacles([
    [0,0,0],
    [0,1,1],
    [0,0,0]
])
print(res)
