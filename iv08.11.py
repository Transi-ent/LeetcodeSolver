class Solution:
    """
    暴力解，回溯
    不好意识，超时了！！！
    """
    def waysToChange(self, n: int) -> int:
        book = [25, 10, 5, 1]

        res = self.traceback(n, book, 0)
        print(res)
        return res

    def traceback(self, n: int, book: list, idx: int) -> int:
        if n<0:
            return 0
        if n==0:
            return 1

        res = 0
        for i in range(idx, len(book)):
            res += self.traceback(n-book[i], book, i)
        return res

class Solution2:
    """
    动态规划，记录之前的计算结果
    见上，0-1 背包问题，有一个二维的状态空间
    """
    def waysToChange(self, n: int) -> int:
        book = [1, 5, 10, 25]
        state = [0]*(n+1)
        state[0] = 1
        for coin in book:
            for i in range(coin, n+1):
                # 当背包容量为 n 时，使用硬币面值为 coin 的组合数等于
                # 当容量为n时只能使用面值比 coin 要小的面值组合数 + 1 （coin>=n）
                state[i] = state[i] + state[i-coin]
        return state[-1]%1000000007







Solution().waysToChange(61)
