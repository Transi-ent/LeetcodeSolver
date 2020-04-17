class Solution:
    """
    递归写法，Exceed Time Limit
    """
    def canJump(self, nums: list) -> bool:
        n = len(nums)
        if n<2:
            return True
        return self.find(nums, 0)

    def find(self, nums: list, index: int) -> bool:
        if index>=len(nums)-1:
            return True

        if nums[index]==0:
            return False

        for i in range(index+1, index+nums[index]+1):
            if self.find(nums, i):
                return True
        return False

class Solution2:
    """
    动态规划, 可惜仍然超时
    """
    def canJump(self, nums: list) -> bool:
        n = len(nums)
        if n<2:
            return True
        memo = [-1]*n
        return self.find(nums, 0, memo)

    def find(self, nums: list, index: int, memo: list) -> bool:
        if memo[index]!=-1:
            return memo[index]

        if index>=len(nums)-1:
            return True

        if nums[index]==0:
            return False

        res = False
        for i in range(index+1, index+nums[index]+1):
            if self.find(nums, i, memo):
                res = True
                break
        memo[index] = res
        return res

class Solution3:
    """
    贪心算法，如果能够到达当前位置，那么一定可以到达当前位置之前的所有位置；
    如果最后能够到达的最远位置大于len(n)，则成功
    """
    def canJump(self, nums: list) -> bool:
        max_dist, n = 0, len(nums)
        for i, d in enumerate(nums):
            if max_dist>=i and i+d>max_dist:
                max_dist = i+d # 如果当前位置是可到达的，且可以更新最大距离，则进行更新
                if max_dist>=n-1:
                    return True
        return False

ret = Solution3().canJump([2,3,1,1,4])
print(ret)







