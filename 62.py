class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1

        memo = [ m*[0]] * n
        memo[0][0] = 1
        for i in range(n):
            for j in range(m):
                if not (i==0 and j==0):
                    if i==0:
                        print("i={}, j={}".format(i,j))
                        memo[i][j] = memo[i][j-1]
                    elif j==0:
                        memo[i][j] = memo[i-1][j]
                    else:
                        memo[i][j] = memo[i-1][j] + memo[i][j-1]
        print(memo)
        return memo[-1][-1]

res = Solution().uniquePaths(3,2)
print(res)
