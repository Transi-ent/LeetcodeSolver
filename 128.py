class Solution:
    """
    哈希表——时间复杂度O(n)
    """
    def longestConsecutive(self, nums: list) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if not num-1 in nums:# 判断该数是不是相连序的数的最小值，
                                    # 不是则不进行处理，相当于进行了剪枝
                tl = 1
                while num+1 in nums:
                    tl += 1
                    num += 1

                res = max(res, tl)
        return res

class Solution2:
    """
    使用排序的方法查看是否超时
    """
    def longestConsecutive(self, nums: list) -> int:
        if len(nums)==0:
            return 0
        nums = list(set(nums))
        nums.sort()
        res = 1
        tl = 1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                tl += 1
                res = max( res, tl )
            else:
                tl = 1
        return res


res = Solution2().longestConsecutive([100, 4, 200, 1, 3, 2])
print(res)
