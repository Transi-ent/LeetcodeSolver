class Solution:
    """
    递归写法
    """
    def massage(self, nums: list) -> int:
        if len(nums)<2:
            return sum(nums)

        return self.findBArrange(nums, 0)

    def findBArrange(self, nums: list, index: int) -> int:
        """
        考虑 nums[index : ] 范围内的预约时间
        :param nums:
        :param index:
        :return:
        """
        if index>=len(nums):
            return 0

        res = 0
        # 在考虑是否取当前 Index 所指的预约时间得两个选择中，取一个最大值
        res = max(
            nums[index] + self.findBArrange(nums, index+2),
            self.findBArrange(nums, index+1)
        )
        return res

class Solution2:
    """
    记忆化搜索
    """
    def massage(self, nums: list) -> int:
        if len(nums) < 2:
            return sum(nums)
        n = len(nums)
        memo = [-1] * n
        memo[-1] = nums[-1]
        return self.findBArrange(nums, 0, memo)

    def findBArrange(self, nums: list, index: int, memo: list) -> int:
        """
        考虑 nums[index : ] 范围内的预约时间
        :param nums:
        :param index:
        :return:
        """
        if index >= len(nums):
            return 0

        if memo[index] != -1:
            return memo[index]
        # 在考虑是否取当前 Index 所指的预约时间得两个选择中，取一个最大值
        res = max(
            nums[index] + self.findBArrange(nums, index + 2, memo),
            self.findBArrange(nums, index + 1, memo)
        )
        memo[index] = res
        return res
















print( Solution2().massage([2,1,4,5,3,1,1,3]) )

