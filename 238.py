class Solution:
    """
    对于元素 nums[i] 来说，分布求得左边元素和右边元素的积，即可得 nums[i] 对应的结果 res[i]
    """
    def productExceptSelf(self, nums: list) -> list:
        left, right = [1]*(len(nums)+1), [1]*(len(nums)+1)
        for i in range(len(nums)):
            left[i+1] = left[i] * nums[i] # left[i] 存放的是 不包含 nums[i] 处所有左边元素的积

        for i in range(len(nums)-1, -1, -1):
            right[i] = right[i+1] * nums[i] # right[i] 存放的是包含 nums[i] 位置处右边所有元素的积

        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i+1])

        print(res)
        return res


Solution().productExceptSelf([1,2,3,4])
