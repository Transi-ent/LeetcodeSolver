class Solution:
    """
    利用数学法：证明当每一小段绳子的长度为3时会得到最大乘积，
    证明地址：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
    """
    def cuttingRope(self, n: int) -> int:
        if n<=3: return n-1
        a, b = n//3, n%3
        if b==0: return 3**a
        if b==1: return (3**(a-1))*4
        return (3**a) * 2

class Solution2:
    """
    使用动态规划
    """
    def cuttingRope(self, n: int) -> int:
        dp = [-1]*(n+1)

        def find(n)->int:
            if dp[n]!=-1:
                return dp[n]
            res = 0
            for i in range(1, n):
                res = max(res, (n-i)*i, i*find(n-i))
            dp[n] = res
            return res
        return find(n)

print(Solution2().cuttingRope(10))
