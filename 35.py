class Solution:
    """
    Binary search
    """
    def searchInsert(self, nums: list, target: int) -> int:
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        left, right = 0, len(nums)-1
        while left<right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid - 1

        while nums[right]<target:
            right += 1
        return right

print(Solution().searchInsert([1,3,5,6], 7))
