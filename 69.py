class Solution:
    """
    线性搜索，时间复杂度 O(N)
    """
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            if i**2 == x:
                return i
            elif i**2>x:
                return i-1


class Solution2:
    """
    牛顿迭代法
    """
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        cur = 1
        while True:
            pre = cur
            cur = (cur + x/cur) / 2
            if abs(cur-pre)<1e-3:
                return int(cur)

res = Solution2().mySqrt(9)
print(res)

