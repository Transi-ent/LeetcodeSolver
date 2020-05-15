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



    #TODO: 6230591 50700 364484
