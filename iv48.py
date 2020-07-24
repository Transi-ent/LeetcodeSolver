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

class Solution2:
    """
    使用滑动窗口，滑动窗口内的字符都是不重复字符，时间复杂度为O(N)的实现;
    使用hash表来记录当前字符出现的位置，因为字符的种类数最多128，所以空间复杂度为O(N);
    这是一个右闭做开的区间；
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        bag, res, left = {}, 0, -1
        for right in range(len(s)):
            if s[right] in bag:
                left = max(left, bag[s[right]])
            bag[s[right]] = right
            res = max(res, right-left)
        return res

print(Solution2().lengthOfLongestSubstring('abcabcbb'))
