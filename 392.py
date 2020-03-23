class Solution:
    """
    因为递归深度过深，会超时
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if s==t=='' or (s=='' and len(t)>0):
            return True
        if s=='' or t=='' or len(s)>len(t):
            return False

        if s[-1]==t[-1]:
            return self.isSubsequence(s[:-1], t[:-1])
        else:
            return self.isSubsequence(s, t[:-1])

class Solution2:
    """
    利用了 iterator 依次取值的特点，会将目标子串的每一个字符取出按顺序进行查找。
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        # 即对于 待查询子串s, 其每一个字符都按序判断是否在迭代器中出现，且一旦出现TRUE，
        # ...迭代器会停止迭代
        return all(i in t for i in s)

class Solution3:
    """
    利用 字符串的 find(str, beg, end) 方法
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        p = -1

        for ch in s:
            p = t.find(ch, p+1)
            if p==-1:
                return False

        return True

class Solution4:
    """
    Double pointers, 两个指针分别指向两个子串
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        l = 0
        while i< len(s) and j<len(t):
            if s[i]==t[j]:
                l += 1
                i += 1
                j += 1
            else:
                j += 1
        return l==len(s)

