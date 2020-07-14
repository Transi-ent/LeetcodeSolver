class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        if len(str)==0 or (not str[0].isdigit() and str[0]!='+' and str[0]!='-'):
            return 0
        neg = None
        if str[0]=="-":
            neg = True
            str = str[1:]
        elif str[0]=='+':
            neg = False
            str = str[1:]
        else:
            neg = False

        res = 0
        for ch in str:
            if ch.isdigit():
                res = 10 * res + int(ch)
            else:
                break
        if neg:
            if res>0x80000000:
                return -2**31
            else:
                return res*(-1)
        else:
            if res>0x7fffffff:
                return 0x7fffffff
            else:
                return res
