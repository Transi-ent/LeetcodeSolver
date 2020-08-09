class Solution:
    def palindromePairs(self, words: list) -> list:
        def isPalindrome(s: str)->bool:
            left, right = 0, len(s)-1
            while left<right:
                if s[left]!=s[right]:
                    return False
                left += 1
                right -= 1
            return True
        res = []
        n = len(words)
        if n<2:
            return res
        for i in range(n-1):
            for j in range(i+1, n):
                if isPalindrome(words[i]+words[j]):
                    res.append([i, j])
                if isPalindrome(words[j]+words[i]):
                    res.append([j, i])

        return res

words = ["abcd","dcba","lls","s","sssll"]
print(Solution().palindromePairs(words))
