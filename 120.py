import copy
class Solution:
    def minimumTotal(self, triangle: list) -> int:
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

class Solution2:
    """
    使用动态规划，dp[i][j] 表示到达位置 [i][j] 处时的最小路径和
    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
    Drawback: 该算法的空间复杂度为O(N^2)

    """
    def minimumTotal(self, triangle: list) -> int:
        if len(triangle)<2:
            return triangle[0][0]

        dp = copy.deepcopy(triangle)
        for i, lyst in enumerate(triangle):
            for j, num in enumerate(lyst):
                if i>0:
                    if j==0:# 对于dp矩阵的第一列元素
                        dp[i][j] = dp[i-1][j] + triangle[i][j]
                    elif j==i:
                        dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                    else:
                        dp[i][j] = min( dp[i-1][j-1], dp[i-1][j] ) + triangle[i][j]
        return min(dp[-1])


class Solution3:
    """
    使用动态规划，dp[i][j] 表示到达位置 [i][j] 处时的最小路径和
    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
    修改方案：因为dp数组是按行计算，triangle数组每次只会用到本行的，不会用之前行数据，所以可以将计算得到的
    dp数组覆盖在 triangle 上，此时空间复杂度为O(1)。
    """

    def minimumTotal(self, triangle: list) -> int:
        if len(triangle) < 2:
            return triangle[0][0]


        for i, lyst in enumerate(triangle):
            for j, num in enumerate(lyst):
                if i > 0:
                    if j == 0:  # 对于dp矩阵的第一列元素
                        triangle[i][j] += triangle[i - 1][j]
                    elif j == i:
                        triangle[i][j] += triangle[i - 1][j - 1]
                    else:
                        triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])






res = Solution().minimumTotal2([[2],[3,4],[6,5,7],[4,1,8,3]])
print(res)



res = Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(res)
