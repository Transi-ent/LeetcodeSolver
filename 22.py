class Solution:
    def generateParenthesis(self, n: int) -> list:
        return self.dfs('', n, n, [])

    def dfs(self, s: str, left: int, right: int, res: list)->list:
        if left==0 and right==0:
            res.append(s)
            return res
        if left:
            self.dfs(s+'(', left-1, right, res)
        if left<right:
            self.dfs(s+')', left, right-1, res)
        return res


res = Solution().generateParenthesis(3)
print(res)
