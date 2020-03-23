class Solution:
    def subsets(self, nums: list) -> list:
        if len(nums)==0:
            return [[]]

        if len(nums)==1:
            return [nums, []]
        res = [[]]
        for k in range(1, len(nums)):
            k_res = []
            k_res = self.findCombinations(nums, k_res, k, [], 0)
            res += k_res

        res.append(nums)
        return res
    def findCombinations(self, nums: list, res: list, k: int, curSubset: list, index: int):
        """
        该题就是在 Combinations 问题的基础之上，不断地变化 k，
        :param nums: 函数输入数组；
        :param res: 结果存放列表；
        :param k: combinations子集的元素个数；
        :param curSubset: 当前正在搜索的子集；
        :param index: 当前应该从 index 位置进行搜索
        :return:
        """
        if len(curSubset)==k:
            res.append(curSubset)
            return res

        for i, em in enumerate(nums[index:]):
            copyOfSubset = curSubset.copy()
            copyOfSubset.append(em)
            self.findCombinations(nums, res, k, copyOfSubset, index+i+1)

        return res

res = Solution().subsets([1,2,3])
print(res)











