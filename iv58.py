class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        n = n%len(s)
        return s[n:]+s[:n]

s = "abcdefg"
k = 2
print(Solution().reverseLeftWords(s, 12))
