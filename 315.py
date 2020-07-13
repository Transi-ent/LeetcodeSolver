class Solution:
    """
    使用Brutal Force，2层for循环
    """
    def countSmaller(self, nums: list) -> list:
        if not nums:
            return []
        counts = []
        n = len(nums)
        for i in range(n-1):
            tmp = 0
            for j in range(i+1, n):
                if nums[i]>nums[j]:
                    tmp += 1
            counts.append(tmp)
        counts.append(0)
        return counts

class Solution2:
    """
    使用Brutal Force，2层for循环
    """
    def countSmaller(self, nums: list) -> list:
        if not nums:
            return []
        counts = []
        n = len(nums)
        for i in range(n-1):

            counts.append( sum([j<nums[i] for j in nums[i+1:]]) )
        counts.append(0)
        return counts

print(Solution().countSmaller([5,2,6,1]))
