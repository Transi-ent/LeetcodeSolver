class Solution:
    """
    使用动态规划：
    状态转移方程：
    1, dp[i][j] 表示模式串p的前i个字符与字符串s的前j个字符的匹配结果；
    2，当p[i]=='?' or p[i]==s[j]时，dp[i][j]=dp[i-1][j-1]；
    3，当p[i]=='*'时，dp[i][j]= dp[i-1][j] | dp[i][j-1]
    """
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        dp =  [[0 for _ in range(ns+1)] for _ in range(np+1)]

        # 初始化, 当模式串的开头为若干个 "*" 时，是可以匹配空字符串的
        dp[0][0] = 1 # 因为当两个字符串都为空时
        for i in range(1, np+1):
            if p[i-1] != "*":
                break
            dp[i][0] = 1

        for i in range(1, np+1):
            for j in range(1, ns+1):
                if p[i-1]==s[j-1] or p[i-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1]=='*':
                    dp[i][j] = dp[i-1][j] | dp[i][j-1]
        return True if dp[-1][-1] else False


print(Solution().isMatch("aa", "*"))
