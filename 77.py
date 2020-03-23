class Solution:
    def combine(self, n: int, k: int):

        res = list()

        self.combinations(set(range(1, n+1)), res, k, set())

        res = [set(i) for i in res]

        return res

    def combinations(self, nums: set, res: list, k: int, tmp_res: set):

        if len(tmp_res)==k:
            if tmp_res not in res:
                res.append(tmp_res)
            return

        for e in nums:
            tmp = nums.copy()
            tmp.remove(e)
            self.combinations(tmp, res, k, tmp_res.union({e}))

    def combine2(self, n: int, k: int) -> list:
        if n<k:
            return []
        if n==k:
            return list(range(1, n+1))

        res = []
        unused = [i for i in range(1, n+1)]

        self.combinations2(res, unused, k, [], 0)

        return res

    def combinations2(self, res:list, n:int, k:int, combin:list, index:int)-> list:
        """
        :param res: 用于存放所有的组合结果；
        :param unused: 尚未使用的数字的集合；
        :param k: 需要递归的深度；
        :param combin: 当前正在搜索的组合结果集；
        :return:
        """
        if len(combin)==k:
            res.append(combin)
            return res

        if index == n:
            return res

        for i, in range(index, n+1):
            copyOfCombin = combin.copy()
            copyOfCombin.append(i)

            self.combinations2(res, n, k, copyOfCombin, i+1)

        return res



res = Solution().combine2(4, 2)
print(res)

