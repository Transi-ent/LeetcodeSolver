# longest substring without repeating characters
# 给定一个字符串，找出这个字符串中最长的无重复元素的最长子串

def longestSubstring(s: str):

    l, r, res = 0, -1, 0 # 滑动窗口，[l ... r], 初始时，滑动窗口内的元素个数需为空

    freq = [0]*256 # 记录出现在滑动窗口中出现的所有字符的频率, ASCII取值在0~255

    while l<len(s):

        if r+1<len(s) and freq[ ord(s[r+1]) ]==0:
            # 滑动窗口右边界未触底，且右边界上的字母在频率表上显示为0
            r+=1
            freq[ord(s[r])]+=1

        else:
            freq[ord(s[l])]-=1
            l-=1

        res = max(res, r+1-l)

    return res

def lengthOfLongestSubstring( s: str) -> int:
    """
    使用滑动窗口，并结合使用一个 hash集合，用于查找已经出现过的字符
    滑动窗口区间为：[left, right]
    :param s:
    :return:
    """
    left, right = 0, -1
    chs = set()
    longest = 0

    while right<len(s) and left<len(s):
        # if right+1-left>longest:
        #     longest = right - left + 1

        if right+1<len(s) and not s[right+1] in chs:
                right += 1 # 0,
                chs.add(s[right])

                longest = max(right - left + 1, longest)

        else:
            #if left<len(s):
            chs.remove(s[left])
            left += 1

    return longest

class Solution:
    """
    使用滑动窗口，记录最长无重复子串的长度(利用左右两个指针left, right，
    当 right 所指字母未出现过，right++，当出现过时，left++，直至right所指的字母
    没有出现过，在这个过程记录，两个指针所代表子串的最大长度)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n<2:
            return n
        left, right = 0, 0
        res, charSet = 1, set(s[0])
        while right<n:
            if right+1>=len(s):
                break
            if not s[right+1] in charSet:
                right += 1
                charSet.add(s[right])
                res = max(res, right-left+1)
            else:
                charSet.remove(s[left])
                left += 1
        return res




res = Solution().lengthOfLongestSubstring("pwwkew")

print(res)







