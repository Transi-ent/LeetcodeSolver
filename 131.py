class Solution:

    def partition(self, s: str) -> list:

        if len(s)==0:
            return []
        if len(s)==1:
            return [[s]]
        lyst = []
        lyst = self.findPalindrome(s, 0, lyst, [])
        return lyst

    def findPalindrome(self, s: str, index: int, lyst: list, raw: list):
        """
        :param s: 函数输入字符串
        :param index: 该函数所处理到的位置索引
        :param lyst: 用于存放结果的列表
        :param raw: 用于存放回文子串的子列表
        :return:
        """
        if index==len(s):
            #raw.append(s[index])
            lyst.append(raw)

            return lyst

        for i in range(len(s)-index):
            seg = s[index: index+i+1]
            if seg and seg == seg[::-1]:
                copy = raw.copy()
                copy.append(seg)
                #print('raw: ',raw, 'c')
                self.findPalindrome(s, index+i+1, lyst, copy)

        return lyst

res = Solution().partition('aab')
print(res)
