class Solution:
    """
    使用列表生成式自带过滤器
    """
    def search(self, nums: list, target: int) -> int:
        return len( [i for i in nums if i==target] )

class Solution2:
    """
    双指针
    """
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            if nums[left]==nums[right]==target:
                return right-left+1
            if nums[left]<target:
                left += 1
            if nums[right]>target:
                right -= 1
        return 0

class Solution3:
    """
    二分搜索
    """
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = -1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                break
            elif nums[mid]<target:
                left = mid
            else:
                right = mid
        if nums[mid]!=target:
            return 0
        left = right = mid
        while left>=0:
            if left-1>=0:
                if nums[left-1]==target:
                    left -= 1
                else:
                    break
            else:
                break
        while right<len(nums):
            if right+1<len(nums):
                if nums[right+1]==target:
                    right += 1
                else:
                    break
            else:
                break
        return right-left+1


print(Solution3().search([5,7,7,8,8,10], 8))
