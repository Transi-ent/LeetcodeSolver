"""
Solution1：在题解46的基础上，将求得的结果去重，或者在添加的时候就不去添加；
Solution2：在进行函数的参数传递时，可以使用数值变量和字符串变量，而非列表，
            其可以放入集合之内，达到去重的目的
"""
class Solution:
    def permuteUnique(self, nums: list) -> list:
        if nums == []:
            return []

        if len(nums) == 1:
            return [nums]

        res = []
        already = set()
        res = self.findPermutation(nums, res, nums.copy(), [], already)
        return res

    def findPermutation(self, nums: list, res: list, remain: list, item: list, already: set):
        """
        :param nums: 函数的输入数组
        :param res: 用于存放结果；
        :param remain: 余下可用的数字；
        :param item: 正在搜索的一条结果
        :return:
        """
        if len(nums) == len(item):
            tmp = [str(n) for n in item]
            id = ''.join(tmp)
            if id not in already:
                res.append(item)
                already.add(id)

        for em in remain:
            copyOfRemain = remain.copy()
            copyOfRemain.remove(em)
            copyOfItem = item.copy()
            copyOfItem.append(em)
            self.findPermutation(nums, res, copyOfRemain, copyOfItem, already)

        return res

res = Solution().permuteUnique([1,1,2])
print(res)
