class Solution:
    """
    超时
    """
    def countDigitOne(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            res += str(i).count('1')
        print(res)
        return res

Solution().countDigitOne(12)
