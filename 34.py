class Solution:
    """
    先使用 二分查找法查找 target 值是否存在，如果存在，记录下索引，并扩展求范围
    ... 不存在直接返回-1
    """
    def searchRange(self, nums: list, target: int) -> list:

        left, right = 0, len(nums)-1
        idx = -1
        while left<=right:
            mid = left + (right - left)//2
            if nums[mid]==target:
                idx = mid
                break
            elif nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1

        print("idx={}".format(idx))
        if idx==-1:
            return [-1, -1]

        right = idx
        left = idx
        while left>0 or right<len(nums)-1:
            print("[{} ... {}]".format(left, right))
            tol = tor = False
            if nums[left-1]==target and left>0:
                left -= 1
                tol = True

            if right<len(nums)-1 and nums[right+1]==target:
                right += 1
                tor = True

            if not tol and not tor:
                break

        print("[{} ... {}]".format(left, right))
        return [left, right]

Solution().searchRange([1,4], 4)
