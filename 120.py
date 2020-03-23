class Solution:
    def minimumTotal(self, triangle: list) -> int:
        #TODO: Wrong, 这是贪心
        pre = 0
        res = 0
        for i in range(len(triangle)):
            if i == 0:
                res += triangle[0][0]
                pre = 0
            else:
                # i >= 1
                if triangle[i][pre]>triangle[i][pre+1]:
                    res += triangle[i][pre+1]
                    pre += 1
                else:
                    res += triangle[i][pre]

        return res

    def minimumTotal2(self, triangle: list) -> int:
        if len(triangle)==0:
            return 0
        if len(triangle)==1:
            return triangle[0][0]
        dp = triangle
        dp[1][0] = dp[0][0] + triangle[1][0]
        dp[1][1] = dp[0][0] + triangle[1][1]
        for i, lyst in enumerate(triangle):
            for j, ele in enumerate(lyst):
                if i>1:
                    if i > j > 0:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
                    elif i == j:
                        dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                    else:
                        dp[i][j] = dp[i-1][j] + triangle[i][j]

        return min(dp[-1])


res = Solution().minimumTotal2([[2],[3,4],[6,5,7],[4,1,8,3]])
print(res)














res = Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(res)
