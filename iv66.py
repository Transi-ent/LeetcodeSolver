class Solution:
    def constructArr(self, a: list) -> list:
        n = len(a)
        b = [0]*n
        left = [1]*(n+1) # left[i+1] 用于存放 a[:i] 项的积
        right = [1]*(n+1) # right[i] 用于存放 a[i:] 项的积
        for i in range(n):
            left[i+1] = a[i]*left[i]

        for i in range(n-1, -1, -1):
            right[i] = a[i]*right[i+1]

        for i in range(n):
            b[i] = left[i] * right[i+1]
        return b

print(Solution().constructArr([1,2,3,4,5]))
