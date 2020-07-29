class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if not nums:
            return []
        start, res = 0, []
        while start+k<=len(nums):
            res.append(max(nums[start: start+k]))
            start += 1
        return res



print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
