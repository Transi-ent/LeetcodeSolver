class Solution:
    """
    使用回溯法穷举
    """
    def translateNum(self, num: int) -> int:
        def traceback(s: str, i: int):
            if i>len(s):# 如果当前索引越界，直接返回0
                return 0
            if i==len(s):
                return 1
            res = 0
            if i+1<len(s) and int(s[i:i+2])<26 and 0<int(s[i]):
                res += traceback(s, i+2)

            return res + traceback(s, i+1)

        s = str(num)
        return traceback(s, 0)

class Solution2:
    """
    使用回溯法穷举
    """
    def translateNum(self, num: int) -> int:
        if num<10:
            return 1
        tmp = num%100
        if tmp<10 or tmp>25: return self.translateNum(num//10)
        else: return self.translateNum(num//10) + self.translateNum(num//100)

res = Solution2().translateNum(25)
print(res)
