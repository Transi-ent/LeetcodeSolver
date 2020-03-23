#TODO: Python中对于引用型变量的函数数值传递是引用传递，无论是否会将该引用型变量返回
#TODO：...都会改变其原始值

class Solution:

    mapping = {
        '0': ' ',
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits: str):
        mapping={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        if not digits:
            return []

        self._letterCombinations(digits, 0, res, mapping, '')

        return res


    def _letterCombinations(self,
                            digits: str,
                            index: int,
                            res: list,
                            mapping: dict,
                            tmp_res: str):

        if index>=len(digits):
            res.append(tmp_res)
            return

        assert index<len(digits), 'str index must be within boundary.'
        chars = mapping[digits[index]]

        for i in range(len(chars)):
            char = chars[i]
            # tmp_res += char

            #print(tmp_res) TODO: 每次都在原字符串的基础上往上加，导致 tmp_res越来越长

            self._letterCombinations(digits, index+1, res, mapping, tmp_res+char)

    def letterCombinations2(self, digits: str) -> list:
        """
        典型的树形问题，在题解的过程中会展开一棵搜索树
        :param digits:
        :return:
        """
        if len(digits)==0:
            return []
        lyst = []
        lyst = self.findCombinations(digits, 0, lyst, '')
        return lyst

    def findCombinations(self, digits: str, index: int, lyst: list, s: str)->list:
        """
        :param digits: Input
        :param index: 对输入的字符串，所达到的搜索的索引位置，
        :param lyst: 所有可能性组合所存放的列表；
        :param s: 当前搜索到的、尚未完成的字符串结果；
        :return:
        """
        if index==len(digits):
            lyst.append(s)
            return lyst

        # 取出当前 index 下的digit对应的所有可能的 letters
        letters = self.mapping[digits[index]]
        for ch in letters:

            self.findCombinations(digits, index+1, lyst, s+ch)

        return lyst


















res = Solution().letterCombinations('23')
print(res)
