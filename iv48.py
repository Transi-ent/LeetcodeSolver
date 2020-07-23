class Solution:
    """
    使用滑动窗口，滑动窗口内的字符都是不重复字符
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        bag, n = set(), len(s)
        left, right = 0, -1 # 窗口范围为[left, right] 左闭右闭区间
        res = 0
        while right<n-1:
            if not s[right+1] in bag:
                right += 1
                bag.add(s[right])
                res = max(res, right-left+1)
            else:
                bag.remove(s[left])
                left += 1

        return res

print(Solution().lengthOfLongestSubstring('abcabcbb'))
