class Solution:
    """
    暴力解，会超时
    """
    def subarraySum(self, nums: list, k: int) -> int:

        res = 0
        for i in range(len(nums)):

            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                if tmp == k:
                    res += 1
        print(res)
        return res

class Solution2:
    """
    构建前缀数组，求任意连续子区间的和
    """
    def subarraySum(self, nums: list, k: int) -> int:

        preArr = (len(nums)+1) * [0]
        for i in range(1, len(preArr)):
            preArr[i] = nums[i-1] + preArr[i-1]

        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if preArr[j+1] - preArr[i]==k:
                    res += 1

        print(res)
        return res

class Solution3:
    """
    构建前缀数组，求任意连续子区间的和
    """
    def subarraySum(self, nums: list, k: int) -> int:

        res = 0
        preDict = {} # 用于存放 【连续子数组和：该子数组和出现次数】对，不记录该和出现的位置
        preDict[0] = 1 # 初始化，前缀为 0 的子数组有一个
        curSum = 0 # 当前搜索到的元素位置子数组和
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum-k in preDict:
                res += preDict[curSum-k]
            if not curSum in preDict:
                preDict[curSum] = 0

            preDict[curSum] += 1
        print(res)
        return res




nums = [1,1,1]
Solution3().subarraySum(nums, 2)
