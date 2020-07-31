class Solution:
    """
    使用对撞指针：
    left 指向从前往后第一个偶数，right指向从后往前第一个奇数
    """
    def exchange(self, nums: list) -> list:
        n = len(nums)
        if n<2:
            return nums
        left, right = 0, n-1
        while left<right:
            if nums[left]%2==1:
                left += 1
            elif nums[right]%2==0:
                right -= 1

            if nums[left]%2==0 and nums[right]%2==1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums



print(Solution().exchange([11,9,3,7,16,4,2,0]))
