class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs)==0:
            return ""
        p1 = 0
        strs.sort()
        while p1<len(strs[0]) and p1<len(strs[-1]):
            if strs[0][p1] == strs[-1][p1]:
                p1 += 1
            else:
                break
        return strs[0][:p1]

class Solution2:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, ch in enumerate(s1):
            if ch != s2[i]:
                return s2[:i]

        return s1


res = Solution().longestCommonPrefix(["dog","racecar","car"])
print(res)
