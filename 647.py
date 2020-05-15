class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):

                ret = self.isPalindrome(s[i: j+1])
                if ret:
                    res += 1
        return res

    def isPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        return s==s[::-1]

class Solution2:

    def countSubstrings(self, s: str) -> int:
        def count(s: str, begin: int, end: int):
            res = 0
            while begin>=0 and end<len(s) and s[begin]==s[end]:
                res += 1
                begin -= 1
                end += 1
            return res

        res = 0
        for i in range(len(s)):
            res += count(s, i, i) # 长度为 奇数 的回文串
            res += count(s, i, i+1)

        print(res)
        return res


    #TODO: 6230591 50700 364484
Solution2().countSubstrings("aaa")
