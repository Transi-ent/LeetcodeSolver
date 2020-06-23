class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def isUgly(n: int) -> bool:
            if n == 1:
                return True
            # n>1
            if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
                return False

            if n % 5 == 0:
                return isUgly(n // 5)
            elif n % 3 == 0:
                return isUgly(n // 3)
            elif n % 2 == 0:
                return isUgly(n // 2)
        th = 0
        num = 0
        while th<n:
            num += 1
            if isUgly(num):
                th += 1
        return num


print(Solution().nthUglyNumber(10))
