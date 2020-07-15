class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**(n)

class Solution2:
    """
    申请内存过大溢出
    """
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            x = 1/x

        memo = [-1]*(n+1)
        memo[:2] = [1, x]
        def pow(x: float, n: int)->float:
            if memo[n] != -1:
                return memo[n]

            if n%2==1:
                res = pow(x, n//2)*pow(x, n//2)*x
            else:
                res = pow(x, n//2)*pow(x, n//2)
            memo[n] = res
            return res

        return pow(x, n)

class Solution3:
    """
    二分法+位运算
    """
    def myPow(self, x: float, n: int) -> float:
        if x==0: return 0
        if n<0: x, n = 1/x, -n
        res = 1
        while n:
            if n&1: res *= x
            x *= x
            n >>= 1
        return res


print(Solution3().myPow(2., -2))
