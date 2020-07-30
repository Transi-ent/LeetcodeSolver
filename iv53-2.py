class Solution:
    def missingNumber(self, nums: list) -> int:

        for i, num in enumerate(nums):
            if i!=num:
                return i

        return len(nums)
