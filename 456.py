class Solution:
    """
    暴力解，三层for循环，肯定会超时
    """
    def find132pattern(self, nums: list) -> bool:

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]<nums[k]<nums[j]:
                        return True
        return False

class Solution2:
    """
    暴力解的优化，使用2层for循环
    """
    def find132pattern(self, nums: list) -> bool:
        if len(nums)<3:
            return False
        i, j, k = 0,0,0
        n = len(nums)
        while i<n:
            while i<n-2 and nums[i]>=nums[i+1]: i += 1
            j = i + 1
            while j<n-1 and nums[j]<=nums[j+1]: j += 1
            k = j + 1
            while k<n:
                if nums[i]<nums[k]<nums[j]:
                    return True
                k += 1
            i = j + 1
        return False


print(Solution2().find132pattern([1,2,3,4,2]))

