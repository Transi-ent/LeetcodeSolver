class Solution:
    """
    不能使用for、while循环
    """
    def sumNums(self, n: int) -> int:
        if n==1:
            return 1
        return n+self.sumNums(n-1)

class Solution2:
    """
    不能使用for、while循环，不能使用乘除，数学法
    """
    def sumNums(self, n: int) -> int:
        return (n**2 + n)>>1

class Solution3:
    """
    不能使用for、while循环，不能使用乘除，数学法
    """
    def sumNums(self, n: int) -> int:
        return sum(range(1, n+1))
