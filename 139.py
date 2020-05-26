class Solution:
    """
    1，使用双指针，递归的搜索单词，每搜索到一个在字典中出现过的单词，就进行下一次递归搜索下一个单词；
    2，此方法本质上是 DFS，它会优先搜索更短的单词，如果完全找到，则返回TRUE；否则会逐层回跳，返回上一层；
    3，最好情况下，一次线性搜索即可返回结果，最差情况下，要完整的搜索一整个完全二叉树才返回结果；
    """
    def wordBreak(self, s: str, wordDict: list) -> bool:
        wordSet = set(wordDict)

        return self.search(s, wordSet, 0)

    def search(self, s:str, wordSet: set, start: int) -> bool:
        if start>=len(s):
            return True
        res = False
        for i in range(start, len(s)): # 每个单词是 s[start: i)
            if s[start: i+1] in wordSet:
                if self.search(s, wordSet, i+1):
                    return True
            elif i==len(s)-1:
                res = res or False

        return res

class Solution2:
    """
    动态规划，使用 dp[] 数组记录之前的搜索状态，dP[i] 存放给定字符串 s[:i] 时的结果
    """
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False]*(len(s)+1) # 状态空间的初始化
        dp[0] = True # 表示空字符可以被字典表示
        for i in range(len(s)):

            for j in range(i+1, len(s)+1):

                if s[i: j] in wordDict and dp[i]:
                    dp[j] = True

        return dp[-1]

class Solution3:
    """
    回溯法递归，使用装饰器缓存计算结果
    """
    def wordBreak(self, s: str, wordDict: list) -> bool:
        import functools
        @functools.lru_cache()
        def traceBack(s: str):
            if not s:
                return True # 若字符串为空，则表明递归到底，搜索到了结果
            res = False
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    res = res or traceBack(s[i:])
            return res

        return traceBack(s)


s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
res = Solution3().wordBreak(s, wordDict)
print(res)
