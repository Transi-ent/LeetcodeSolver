class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

class Solution2:
    """
    位运算速度更快
    """
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        while b:
            c = (a&b)<<1 # 求a，b 的进位和
            a = a^b # 求出 a, b 的非进位和
            b = c
        return bin(a)[2:]




res = Solution2().addBinary("11", '1')
print(res)
