class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        if len(coins)<1 or amount<1:
            return -1
        n = len(coins)
        memo = [ [float('inf')]*(n) for _ in range(amount+1) ]

        for i in range(n):
            memo[0][i] = 0

        for i in range(1, amount+1):
            for j in range(n):
                if i>coins[j]:
                    # 随着所需兑换金额的不断增加，搜索所需硬币组合空间
                    # memo[i] 表示为了兑换金额为 i 的数目，所有硬币组合的数目列表
                    memo[i][j]=min(memo[i-coins[j]])+1

        return min(memo[-1]) if min(memo[-1]) != float('inf') else -1


class Solution2:
    def coinChange(self, coins: list, amount: int) -> int:
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            dp[i] = min( dp[i-c] if i>=c else float('inf') for c in coins ) + 1

        return dp[-1] if dp[-1]!=float('inf') else -1











