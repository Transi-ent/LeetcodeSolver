class Solution:
    """
    未排序的列表与已排序的列表作对比，使用双指针，不同的连续子数组即为结果。
    已找到的最短子数组中所有的值都大于该数组左边的元素值，该子数组所有的值都小于该数组右边所有的值。
    """
    def findUnsortedSubarray(self, nums: list) -> int:
        sortedArr = sorted(nums)
        left, right = 0, len(nums)-1
        while left<right and nums[left]==sortedArr[left]:
            left += 1

        while left<right and nums[right]==sortedArr[right]:
            right -= 1

        return 0 if left == right else right - left + 1


nums = [1,3,2,2,2]
res = Solution().findUnsortedSubarray(nums)

print(res)
