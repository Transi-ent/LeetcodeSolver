class Solution:
    """
    1, 因为Alice最后一次能够抽牌一定是在得分为K-1的时候，这时能够得到的最大的牌为 K+W-1，且得分从0开始;
    2, 且得分在[k, k+w-1]范围内，大于NAlice输，小于NAlice赢，求Alice赢的概率
    3， dp[i]表示在得分为i时Alice赢的概率
    4， dp[i] = 1/W * (dp[i+1]+dp[i+2]+dp[i+3]+...+dp[i+W])
    """
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [-1]*(K+W)# dp[i]表示在得分为i时Alice赢的概率
        s = 0
        for i in range(K, K+W):
            dp[i] = 1 if i<=N else 0
            s += dp[i]

        for i in range(K-1, -1, -1):# 从索引K-1开始一直到0，倒序计算
            dp[i] = s/W
            s = s - dp[i+W] + dp[i]

        return dp[0]

res = Solution().new21Game(21, 17, 10)
print(res)
