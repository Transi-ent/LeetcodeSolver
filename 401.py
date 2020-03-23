class Solution:

    # def readBinaryWatch(self, num: int) -> list:
    #
    #     pass
    #
    # def combinations(self, h: int, m: int)-> list:
    #     """
    #     在 h 和 m 传入之前，先检验其数值的合法性， 0<=h<=4, 0<=m<=6
    #     :param h: 表示小时的灯个数；
    #     :param m: 表示分钟的灯个数
    #     :return:
    #     """
    #     permutationOfHour=[]
    #     permutationOfHour = self.findCombinations(permutationOfHour, 2, 4, [0,0,0,0], 0)
    #     print(permutationOfHour)
    #
    #
    # def findCombinations(self, res: list, nOfOn: int, n: int, curOn: list, index: int)-> list:
    #     """
    #     搜索得到不同的 灯 Permutations
    #     :param nOfOn: 该类灯亮的个数；
    #     :param n: 该类灯的个数；
    #     :param index: 搜索进行到的位置索引；
    #     :return:
    #     """
    #     if sum(curOn)==nOfOn:
    #         res.append(curOn)
    #         return res
    #
    #     for i in range(index, n):
    #         copyOfCurOn = curOn.copy()
    #         copyOfCurOn[i] = 1
    #         self.findCombinations(res, nOfOn, n, copyOfCurOn, index+1)
    #
    #     return res
    def readBinaryWatch(self, num: int) -> list:
        return [f'{h}:{m:02>d}' for h in range(12) for m in range(60) if (bin(h)+bin(m)).count('1')==num]



res = Solution().combinations(2,2)
