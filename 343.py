class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1]*(n+1)
        #global memo
        return self.breakInteger(n, memo)

    # 将一个正整数n, 拆分成至少两个正整数的和
    def breakInteger(self, n, memo):
        # 递归终止条件，当n不能够被继续分割
        if n==1:
            return 1

        # 当n>=2时
        if memo[n]!=-1:
            return memo[n]
        res = 1
        for i in range(1, n):
            # 进行比较，看是不进行拆分比较大，是拆分为2个比较大，还是拆分成3个及以上比较大
            res = max(res, i*(n-i), i*self.breakInteger(n-i, memo))
        memo[n] = res

        return res


class Solution2:
    def integerBreak(self, n: int) -> int:

        memo = [-1] * (n+1)
        memo[1]=1
        if n==1:
            return memo[1]
        memo[2] = 1
        return self.breakNum(memo, n)

    def breakNum(self, memo: list, n: int)-> int:

        if memo[n] != -1:
            return memo[n]

        tmpMax = -1
        for i in range(1, n):
            if memo[n - i] != -1:
                # TODO: 易将 i*(n-i) 这一项漏掉，会将传入函数 breakNum() 的数字一直进行分割
                tmpMax = max(memo[n-i] * i, i*(n-i), tmpMax)

            else:
                memo[n-i] = self.breakNum(memo, n-i)

        memo[n] = tmpMax
        return tmpMax
