class Solution:
    """
    使用位运算：
    1. 求进位和 ———— 与运算；
    2. 求非进位和 ———— 异或运算
    """
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a&x, b&x# 对输入的数字进行截取，只取其后32位
        while b:
            c = ((a&b)<<1)&x # 求出 a, b 两个数的进位和
            a = a^b # 求出 a, b 两个数的非进位和
            # a, b = a^b, (a&b)<<1
            b = c
        return a if a<=0x7fffffff else ~(x^a)

print(Solution().add(-1, 2))
