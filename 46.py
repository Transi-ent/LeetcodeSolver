"""
Python 函数对于引用型变量的传递，是引用传递，在传参时传的是地址
TODO：在函数内部改变引用型变量的值，那么该变量就被永久性的改变了

TODO: 回溯的明显特征，在循环中递归的调用自己。
"""

class Solution:
    def permute(self, nums: list):

        res = list()

        self.permu(set(nums), res, [])

        return res

    def permu(self, nums: set, res: list, tmp_res):

        if len(nums)==0:
            res.append(tmp_res)
            return

        lyst = list(nums)
        for item in lyst:
            self.permu(nums-{item}, res, tmp_res+[item])

    def permute2(self, nums: list) -> list:
        if nums==[]:
            return []

        if len(nums)==1:
            return [nums]

        res = []
        res = self.findPermutation(nums, res, nums.copy(), [])
        return res

    def findPermutation(self, nums: list, res: list, remain: list, item: list):
        """
        :param nums: 函数的输入数组
        :param res: 用于存放结果；
        :param remain: 余下可用的数字；
        :param item: 正在搜索的一条结果
        :return:
        """
        if len(nums)==len(item):
            res.append(item)

        for em in remain:
            copyOfRemain = remain.copy()
            copyOfRemain.remove(em)
            copyOfItem = item.copy()
            copyOfItem.append(em)
            self.findPermutation(nums, res, copyOfRemain, copyOfItem)

        return res

class Solution2:
    def permute(self, nums: list) -> list:

        return self.findPermutation(set(nums), [], [])

    def findPermutation(self, s: set, tmp: list, res: list)->list:
        """
        :param nums:
        :param s: 可用元素集合；
        :param tmp: 还未完整的一个数列；
        :param res: 存放结果
        :return:
        """
        if len(s)==0:
            res.append(tmp)
            return res

        nums = list(s)
        for num in nums:
            copyOfS = s.copy()
            copyOfS.remove(num)
            copyOfList = tmp.copy()
            copyOfList.append(num)
            self.findPermutation( copyOfS, copyOfList, res)
        return res

class Solution3:
    def permute(self, nums: list) -> list:
        res = []
        def traceback(nums: list, tmp: list):
            if not nums: # 若 nums 数组为空，说明当前组合搜索已经到底
                res.append(tmp)
                return
            for i in range(len(nums)):
                traceback(nums[:i]+nums[i+1:], tmp+[nums[i]])

        traceback(nums, [])
        return res


res = Solution3().permute([1,2,3])
print(res)
