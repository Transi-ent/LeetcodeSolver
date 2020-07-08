class Solution:
    """
    使用递归，建立一棵递归树
    """
    def permutation(self, s: str) -> list:
        def dfs(s: str, tmp: str):
            if len(s)==0:
                if not tmp in visited:
                    res.append(tmp)
                    visited.add(tmp)
                return
            for i, ch in enumerate(s):
                dfs(s[:i]+s[i+1:], tmp+ch)
            return
        res = []
        visited = set()
        dfs(s, "")
        return res

print(Solution().permutation("aac"))
