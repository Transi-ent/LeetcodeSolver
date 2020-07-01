class Solution:
    """
    没有更好的办法，先上暴力解
    使用动态规划，状态空间为 len(A)*len(B)的 2 维列表
    """
    def findLength(self, A: list, B: list) -> int:
        dp = [[0]*len(A) for _ in range(len(B))]
        for i in range(len(B)):
            for j in range(len(A)):
                if i==0:
                    if A[j]==B[i]:
                        dp[i][j] = 1
                else:
                    if A[j] == B[i]:
                        if j==0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i-1][j-1] + 1
        return max( [max(ly) for ly in dp] )

class Solution2:
    """
    继续使用动态规划，优化状态空间，因为状态空间每次只会用到上一行，所以状态空间为len(A)*2，更加节省内存
    """
    def findLength(self, A: list, B: list) -> int:
        MAX = 0
        dp = [0 for _ in range(len(A)+1)]
        for i in range(1, len(B)+1):
            for j in range(len(A), 0, -1):
                if A[j-1] == B[i-1]:
                    dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0
            MAX = max(MAX, max(dp))
        return MAX


A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(Solution2().findLength(A, B))
