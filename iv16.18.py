class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        # 1、pattern为空时
        if len(pattern)==0:
            return len(value)==0
        # 2. pattern 不为空时
        # 2.1 value 为空，判断pattern是否为一个字母组成
        if len(value)==0:
            i = 0
            while i<len(pattern) and pattern[i]==pattern[0]:
                i += 1
            return i==len(pattern)# 当pattern字符串由一个字母组成时，返回true
        # 2.2 pattern不为空，value不为空时
        n, m = len(pattern), len(value)
        #   统计pattern字符串中a、b的个数
        na, nb = pattern.count('a'), pattern.count('b')
        # 2.2.1 判断是否存在 pattern 字符串中仅存在一种字母的情况
        if na==0: return self.helper(value, nb)
        elif nb==0: return self.helper(value, na)

        # 2.2.2 使得pattern字符串中的a或b为空时，判断是否通过
        if self.helper(value, na): return True
        if self.helper(value, nb): return True

        # 2.2.3 a、b都不为空时分别枚举ab的长度进行匹配
        for ia in range(1, m):
            if ia*na+nb>m: break
            if (m-ia*na)%nb!=0: continue
            ib = (m-ia*na)%nb
            if self.check(pattern, value, ia, ib):
                return True
        return False

    def helper(self, value: str, k: int) -> bool:
        # 在pattern和value都不为空的情况下，判断value是否可以被pattern k次完整切分
        # 该函数处理的都是pattern字符串内只有一种字母
        m = len(value)
        if m%k!=0: return False
        times = m//k
        for i in range(times, m, times):
            if value[i: i+times] != value[:times]: return False
        return True

    def check(self, pattern: str, value: str, ia: int, ib: int)->bool:
        ps = ["", ""] # 分别用于存放a, b 匹配的字符串
        j = 0
        for i in range(len(pattern)):
            if pattern[i]=='a':
                if ps[0]=="":
                    ps[0] = value[j: ia]
                elif ps[0] != value[j: ia]:
                    return False
                j += ia
            elif pattern[i]=='b':
                if ps[1]=="":
                    ps[1] = value[j: ib]
                elif ps[1]!=value[j: ib]:
                    return False
                j += ib
        return True

print(Solution().patternMatching("abba", "dogcatcatdog"))
