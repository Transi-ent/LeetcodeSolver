class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "
        map = {}
        for ch in s:
            map[ch] = map.get(ch, 0) + 1

        map = {k:v for k, v in map.items() if v==1}
        for ch in s:
            if ch in map:
                return ch
        return ""


print(Solution().firstUniqChar("cc"))
