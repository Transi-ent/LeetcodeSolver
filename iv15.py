class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n&1
            n = n>>1
        return res

print(Solution2().hammingWeight(3))
