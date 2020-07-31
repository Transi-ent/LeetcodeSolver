class Solution:
    """
    当存在以下情况时当前字符串代表不了数字:
    1，出现不是e/E的字母;
    2，出现1个以上的符号；
    3，出现一个以上的".";
    4，e后面的数字需要是整数，前面的数字可以是小数；

    """
    def isNumber(self, s: str) -> bool:
        def isFloat(s: str) -> bool:
            """
            有且仅有一个小数点
            """
            dot = 0
            n = 0
            for ch in s:
                if ch.isdigit():
                    n += 1
                elif ch=='.':
                    dot += 1

            return dot+n==len(s) and dot==1 and n!=0

        s = s.strip()
        if not s:
            return False
        if s[0]=='+' or s[0]=='-':
            s=s[1:]

        # 1. 当前字符串全部是数字
        if s.isdigit():
            return True

        # 2. 检查是否包含小数点和e/E
        # 2.1 检查小数点或字母E的数量是否过量
        n_dot = s.count('.')
        n_e = s.count('e') + s.count('E')
        if n_dot>1 or n_e>1:
            return False
        # 2.2 当仅有一个小数点时
        if n_e==1:
            idx = s.index('e') if 'e' in s else s.index('E')
            if idx==len(s)-1:
                return False
            if s[idx+1] in ('+', '-'):
                #print(11111)
                if (s[:idx].isdigit() or isFloat(s[:idx])) and s[idx+2:].isdigit():
                    return True
            else:
                #print(22222)
                if (s[:idx].isdigit() or isFloat(s[:idx])) and s[idx+1:].isdigit():
                    return True
        if n_dot==1:
            if isFloat(s):
                return True

        return False

class Solution2:
    """
    该题解来自LeetCode 评论区，太 TM 牛皮了
    """
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False

print(Solution().isNumber(" e"))
