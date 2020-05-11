class Solution:
    """
    时间复杂度 O(N)，会超时
    """
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            x = 1/x
        res = 1
        for i in range(n):
            res = res * x
        return res

class Solution2:
    """
    时间复杂度降低了，但是使用了过多的内存
    """
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            x = 1/x
        memo = [-1]*(n+1)
        return self.compute(memo, n, x)
    def compute(self, memo: list, n: int, x: float) -> float:
        if memo[n]!=-1:
            return memo[n]
        if n==0:
            return 1
        if n==1:
            return x
        memo[n] = self.compute(memo, n//2, x) * self.compute(memo, n-n//2, x)
        return memo[n]

class Solution3:
    """
    使用分治法，每次先求 x的n//2次幂，如果n为奇数，还需要额外的乘以x;
    例如要求 x 的 77次幂，可以先求得它的38次幂再乘以x，要求的它的 38 次幂就要先求得...
    ...它的19次幂，==> 求得 9 次幂再乘以 x，==> 求得 4 次幂再乘以 x，==> ...
    时间复杂度 O(logN)
    """
    def myPow(self, x: float, n: int) -> float:
        def divAndConquer(N): # 利用 Python 的闭包，内部函数可以使用外部函数的变量
            if N==0:
                return 1.0

            # 当 N 不为 0 时
            y = divAndConquer(N//2)
            return y*y if N%2==0 else y * y * x

        return divAndConquer(n) if n>0 else 1.0/divAndConquer(-n)





res = Solution3().myPow(2, 10)
print(res)
