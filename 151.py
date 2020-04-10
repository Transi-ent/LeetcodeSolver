class Solution:
    def reverseWords2(self, s: str) -> str:
        if not s.strip():
            return ''
        res = ''
        s = ' ' + s.rstrip()
        end = len(s)
        for i in range(end-1, -1, -1):
            if s[i]==' ' and s[i+1]!=' ':
                res += s[i+1: end]
                res += ' '
                end = i
            elif s[i]==' ':
                end = i

        print(res)
        return res.strip()
    def reverseWords(self, s: str) -> str:

        res = ''
        s = ' ' + s.rstrip()
        end = len(s)
        for i in range(end-1, -1, -1):
            if s[i]==' ':
                if i+1<len(s) and s[i+1]!=' ':
                    res += s[i+1: end]
                    res += ' '


                end = i

        print("res:",res, len(res))
        return res.strip()


Solution().reverseWords(" ")
