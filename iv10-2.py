class Solution:
    """
    fibnacchi问题
    """
    def numWays(self, n: int) -> int:
        if n<2:
            return 1
        a, b = 1, 1
        for i in range(n-1):
            a, b = b, a+b

        return b

print(Solution().numWays(7))
