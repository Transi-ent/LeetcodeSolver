class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2:
            return s
        res = s[0]
        for i in range(n):
            tmp1 = s[i]
            j = 1
            while 0<=i-j and i+j<n:
                # 回文串搜索不越界
                if s[i-j]==s[i+j]:
                    tmp1 = s[i-j]+tmp1+s[i+j]
                    j += 1
                else:
                    break

            if len(tmp1)>len(res):
                res = tmp1

            if i+1<n and s[i]==s[i+1]:
                tmp2 = s[i: i+2]
                l, r = i-1, i+2 # 闭区间索引
                while 0<=l and r<n:
                    if s[l]==s[r]:
                        tmp2 = s[l] + tmp2 + s[r]
                        l -= 1
                        r += 1
                    else:
                        break
                if len(tmp2)>len(res):
                    res = tmp2

        print(res)
        return res

Solution().longestPalindrome("cbbd")
