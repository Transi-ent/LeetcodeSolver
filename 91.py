class Solution:
    #TODO: Fibonacchi sequence.
    def numDecodings(self, s: str) -> int:
        if s is '':
            return 0
        if len(s)==1:
            if s=='0':
                return 0
            else:
                return 1
        memo = [-1] * (len(s)+1)
        if memo[0]=='0':
            memo[0] = 0
        else:
            memo[0] = 1
        if 11<=int(s[:2])<=26:
            memo[1] = 2
        elif 1<=int(s[:2])<=10 or 27<=int(s[:2]):
            memo[1] = 1
        else:
            memo[1] = 0

        return self.fib(memo, len(s)-1, s)
    def fib(self, memo: list, n: int, s: str) -> int:
        """
        :param memo: 用于存储结果，i 位置上 --> s[:i]字符串对应的编码总数
        :param index: 当前应该处理的索引位置
        :return:
        """
        if memo[n] != -1:
            return memo[n]
        if s[n]=='0':
            return memo[n-1]

        if 11<=int(s[n-1: n+1])<=26:
            memo[n] = memo[n-1] + memo[n-2]
        else:
            memo[n] = memo[n-1]
        return memo[n]

class Solution2:
    def numDecodings(self, s: str) -> int:
        # 加上虚拟头部，避免对头部进行特殊处理
        memo = [1, 1] + [0] * len(s)
        s = '99' + s
        for i in range(2, len(s)):
            if 11<=int( s[i-1: i+1] )<=26:
                memo[i] += memo[i-2]

            if s[i] != '0':
                memo[i] = memo[i-1]

        return memo[-1]



res = Solution().numDecodings('27')
print(res)










