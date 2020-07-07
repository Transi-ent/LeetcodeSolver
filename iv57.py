class Solution:
    """
    使用对撞指针———— 一前一后两个指针(因为是有序数组)，left, right
    当两个指针所对应的两个数的和较小时，左指针往右移动，当和较大时，右指针往左移动；
    当两个指针相撞仍为找到时，表示不存在
    """
    def twoSum(self, nums: list, target: int) -> list:
        left, right = 0, len(nums)-1
        while left<right:
            tmp = nums[left]+nums[right]
            if tmp==target:
                return [nums[left], nums[right]]
            elif tmp<target:
                left += 1
            else:
                right -= 1
        return None
