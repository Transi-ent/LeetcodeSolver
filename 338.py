class Solution:
    """
    利用 Python API
    """
    def countBits(self, num: int) -> list:
        res = []
        for i in range(num+1):
            res.append(bin(i)[2:].count('1'))
        return res

class Solution2:
    """
    利用移位运算和奇偶数的二进制码的性质；
    if n%2==0, so f(n) = f(n/2), 因为一个数增大2倍，只会进行移位运算，不会改变 1 的个数；
    if n%2==1, so f(n) = f(n-1) + 1, 一个奇数必然是偶数+1所得，且偶数的二进制位的最低位
    ...为0，+1后不会进 1 。
    """
    def countBits(self, num: int) -> list:
        res = [0]
        for i in range(1, num+1):
            if i%2==1:
                res.append(res[i-1]+1)
            else:
                res.append(res[i//2])

        return res
