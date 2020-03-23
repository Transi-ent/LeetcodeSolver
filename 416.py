class Solution:
    """
    从数组 nums 中挑出若干个数，是这些数的和为 sum(nums)/2,
    先写出递归的写法，然后搞出记忆化搜索的版本
    """
    def canPartition(self, nums: list) -> bool:
        if len(nums)<2:
            return False
        sum1 = sum(nums)
        if sum1%2 != 0:
            return False
        # 将初始状态空间全部置为-1，之后正式填充时0->False, 1->True
        memo = [[-1]*(sum1//2 +1) for _ in range(len(nums))]
        for i in range(sum1//2 + 1):
            if i==nums[0]:
                memo[0][i]=1
            else:
                memo[0][i]=0

        return self.tryPartition(nums, len(nums)-1, sum1//2, memo)

    def tryPartition(self, nums: list, index: int, sum: int, memo: list) ->bool:
        if index<0:
            return False
        if sum==0:
            return True

        if memo[index][sum]!=-1:
            return memo[index][sum]==1

        res = self.tryPartition(nums, index-1, sum, memo) or\
            self.tryPartition(nums, index-1, sum-nums[index], memo)
        memo[index][sum] = res
        return res

class Solution2:
    """
    自底向上的动态规划写法；
    本质其实就是搜索并填充状态空间，状态空间是一维的，就去搜索一维的状态空间（使用一层for循环）
    ...状态空间是二维的，就使用两层for循环去搜索状态空间。状态空间应该是压缩之前的，比如，
    ...这里的状态有数组的元素和sum取值，两个状态量。 0-1背包问题有背包体积和物品重量两个状态量
    """
    def canPartition(self, nums: list) -> bool:
        if len(nums)<2:
            return False
        sum1 = sum(nums)
        if sum1%2 != 0:
            return False
        # 将初始状态空间全部置为-1，之后正式填充时0->False, 1->True，状态空间可压缩
        c = (sum1//2)
        n = len(nums)
        memo = [False] * (c+1)
        for i in range(sum1//2 + 1):
            memo[i]= ( i == nums[0] )

        for i in range(1, n):
            for j in range(c, -1, -1):
                if j>=nums[i]:
                    """
                    当前的memo[j]是否为TRUE，是不考虑当前元素和考虑当前元素的共同结果
                    """
                    memo[j] = memo[j] or memo[j-nums[i]]
        return memo[-1]


print(Solution2().canPartition([1,5,11,5]))
