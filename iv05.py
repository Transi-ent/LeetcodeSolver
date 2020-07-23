class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

class Solution2:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for ch in s:
            if ch==' ':
                res += '%20'
            else:
                res += ch
        return res
print(Solution().replaceSpace('we are happy'))
