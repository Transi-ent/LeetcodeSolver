class Solution:
    """
    Brutal Force:
    遍历任意两个数组索引，进行比较，以求得最大值. 区间左闭右闭 []
    TODO：超时了
    """
    def maxSubArray(self, nums: list) -> int:
        n, res = len(nums), float('-inf')
        if n<2:
            return sum(nums)
        for i in range(n):
            tmp = nums[i]
            res = max(res, tmp)
            for j in range(i+1, n):
                tmp += nums[j]
                res = max(res, tmp)

        return res

class Solution2:
    """
    动态规划：
    1. 定义状态：dp[i] 表示以nums[i]为结尾的连续子数组的和
    2. 状态转移方程：
        当dp[i-1]<0, dp[i] = nums[i]
        当dp[i-1]>0, dp[i] = dp[i-1]+nums[i]
    """
    def maxSubArray(self, nums: list) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        return max(nums)

nums = [-2,1,]
print(Solution().maxSubArray(nums))
