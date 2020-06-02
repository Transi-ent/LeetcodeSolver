class Solution:
    """
    不能使用for、while循环
    """
    def sumNums(self, n: int) -> int:
        if n==1:
            return 1
        return n+self.sumNums(n-1)
