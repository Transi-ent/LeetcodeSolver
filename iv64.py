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
    不能使用for、while循环，数学法
    """
    def sumNums(self, n: int) -> int:
        return (1+n)*(n)//2
