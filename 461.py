class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin( x^y ).count('1')

class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        xb = bin(x)[2:]
        yb = bin(y)[2:]
        l = max( len(xb), len(yb) )

        xb = xb.zfill(l)
        yb = yb.zfill(l)
        res = 0
        for i in range(l):
            if xb[i] != yb[i]:
                res += 1

        return res


