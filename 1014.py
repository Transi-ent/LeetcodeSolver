class Solution:
    """暴力解"""
    def maxScoreSightseeingPair(self, A: list) -> int:
        res = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                res = max(res, A[i]+A[j]+i-j)
        print(res)
        return res

class Solution2:
    """动态规划解法"""
    # 因为i、j之间总是具有顺序性，i总是在j的前面，总是一左一右，
    # 当出现一个比当前的左边更大的一个值时，对左边的值进行更新
    # 在左边的值为最大的情况下，依次搜索右边的值，以求得最大的评分
    def maxScoreSightseeingPair(self, A: list) -> int:
        res = 0
        MAX = A[0]
        for i in range(1, len(A)):
            res = max(res, MAX + A[i]-i)
            if A[i]+i>MAX:
                MAX = A[i] + i
        print(res)
        return res

Solution2().maxScoreSightseeingPair([8,1,5,2,6])
