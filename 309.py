class Solution:
    """
    动态规划：状态机，规定状态1只能转向状态2，则必然会有1天的冷却期
    状态   \   第i天    | 0         | ...  |  i-1       |  i   |  ...  |   n
     0(持有)           | -price[0] | ...  | dp[i-1][0] | dp[i][0]= max(dp[i-1][0], dp[i-1][2]-price[i])
     1(不持有，冷却/卖出)     |  0        | ...  | dp[i-1][1] | dp[i][1]= dp[i-1][0]+price[i]
     2(不持有，可买入)   |  0        | ...  | dp[i-2][2] | dp[i][2] = max(dp[i-1][2], dp[i-1][1])

    """
    def maxProfit(self, prices: list) -> int:
        if not prices or len(prices)<2:
            return 0
        # 使用动态规划求解，状态机有3种状态——0、1、2
        memo = [ [0 for _ in range(3)] for _ in range(len(prices))]
        # 对于初始的0状态，还没有机会卖出
        memo[0][0] = -prices[0]
        for i in range(1, len(prices)):
            # 第i天的持有状态来自于第i-1天的持有状态，与第i-1不持有可买入状态
            memo[i][0] = max( memo[i-1][0], memo[i-1][2]-prices[i])
            memo[i][1] = memo[i-1][0] + prices[i]
            memo[i][2] = max( memo[i-1][2], memo[i-1][1] )

        return max(memo[-1][1:])

class Solution2:
    """
    压缩状态空间，使用3个变量代替二维的状态空间
    """
    def maxProfit(self, prices: list) -> int:
        if not prices or len(prices)<2:
            return 0
        s0, s1, s2 = -prices[0], 0, 0
        for i in range(1, len(prices)):
            f0 = max( s0, s2-prices[i] )
            f1 = s0 + prices[i]
            f2 = max(s2, s1)
            s0, s1, s2 = f0, f1, f2
        return max(s1, s2)


print(Solution2().maxProfit([1,2,3,0,2]))
