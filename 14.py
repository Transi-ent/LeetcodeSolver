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

res = Solution().longestCommonPrefix(["dog","racecar","car"])
print(res)
