import re
class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if not s or s[0].isalpha():
            return 0
        s = ( s.split(' ')[0] )
        if (s.startswith('-') or s.startswith('+')):
            if len(s)==1 or not s[1].isnumeric():
                return 0
        if '.' in s:
            s = s.split('.')[0]
        if not s or s[0].isalpha():
            return 0
        for i in range(len(s)):
            if i==0:
                if s[0] in {'-', '+'} or s[0].isnumeric():
                    continue
                else:
                    return 0
            else:
                print("s:{}, i:{}".format(s, i))
                if not s[i].isnumeric():
                    s = s[:i]
                    break
        res = int(s)
        # 取值范围越界
        if res<-2**31:
            return -2**31
        elif res>2**31-1:
            return 2**31-1
        else:
            return res

class Solution2:
    """
    re: 用于处理正则表达式的模块
    \^: 匹配字符串的开头
    [\-\+]: 匹配 '-'，'+'z中的一个
    ?: 前面的模式出现一次或没有，相当于对前面的模式取 True 操作；
    \d: 匹配数字；
    +： 前面的模式至少匹配一次；
    """
    def myAtoi(self, s: str) -> int:
        lyst = re.findall('^[\-\+]?\d+', s.strip())
        if lyst:
            res = lyst[0]
        else:
            return 0
        return max( min(int(res), 2**31-1), -2**31 )

res = Solution2().myAtoi("words and 987")
print(res)
