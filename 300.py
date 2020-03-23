class Solution:
    """
    memo[i] 用于存放以 nums[i] 为结尾的最长子序列长度
    """
    def lengthOfLIS(self, nums: list) -> int:
        # 每个数字都是长度为1的子序列
        memo = [1]*len(nums)
        n = len(nums)
        if n<=1:
            return n

        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    memo[i] = max(memo[i], 1+memo[j])

        return max(memo)
