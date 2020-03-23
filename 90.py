class Solution:
    """
    问题78的延伸，可以将每个 combination 的结果连接成一个字符串，
    ...并将该字符串放进一个集合内，以去重~
    """
    def subsetsWithDup(self, nums: list) -> list:
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [nums, []]
        res = [[]]
        nums.sort()
        for k in range(1, len(nums)):
            k_res = set()
            k_res = list(self.findCombinations(nums, k_res, k, [], 0))
            # print('k:',k, '  combinations:',k_res)
            k_res = [list(em) for em in k_res]
            res += k_res

        res.append(nums)
        return res

    def findCombinations(self, nums: list, res: set, k: int, curStr: list, index: int):
        """
        该题就是在 Combinations 问题的基础之上，不断地变化 k，
        :param nums: 函数输入数组；
        :param res: 结果存放列表；
        :param k: combinations子集的元素个数；
        :param curSubset: 当前正在搜索的子集；
        :param index: 当前应该从 index 位置进行搜索
        :return:
        """
        if len(curStr) == k:
            res.add(tuple(curStr))
            return res

        for i, em in enumerate(nums[index:]):

            copyOfCurlist = curStr.copy()
            copyOfCurlist.append(em)
            self.findCombinations(nums, res, k, copyOfCurlist, index + i + 1)
        return res


res = Solution().findCombinations([4,4,4,1,4],set(),2,[],0)
print(res)













