class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1]*(n+1)
        memo[1] = 1
        if n==1:
            return memo[1]
        memo[2] = 2
        if n==2:
            return memo[2]
        for i in range(3, n+1):
            memo[i] = memo[i - 2] + memo[i - 1]

        print(memo)
        return memo[n]

    def climbStairs2(self, n: int) -> int:
        memo = [-1] * (n+1)
        memo[1] = 1
        if n==1:
            return memo[1]
        memo[2] = 2
        if n==2:
            return memo[2]
        res = self.findWays(memo, n)

        return res

    def findWays(self, memo: list, n: int) -> int:
        if memo[n] == -1:
            memo[n] = self.findWays(memo, n - 1) + self.findWays(memo, n - 2)

        return memo[n]

res = Solution().climbStairs(3)
print(res)
