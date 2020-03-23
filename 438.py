# Find all anagrams in a string,
# 给定一个字符串s和一个非空字符串p，在S中找出所有P的anagrams子串，并返回这些子串的起始索引
from collections import Counter

def findAllAnagrams(s: str, p:str):
    # 固定长度的滑动窗口

    l, res, n, np = 0, [], len(s), len(p)

    freq = Counter(s[:np])

    dp = Counter(p)

    while l+np-1<n:

        # 判断滑动串口内的词频是否与字符串P的词频相同
        if freq==dp:
            res.append(l)

        freq[s[l]]-=1
        l+=1

    return res


def findAnagrams(s: str, p: str) -> list:
    """
    使用滑动窗口，统计窗口区间内的词频，和非空字符串p的词频，
    ..若两个词频相同，则记录滑动窗口左指针的位置
    :param s:
    :param p:
    :return:
    """
    left, right, res = 0, len(p)-1, list()

    dicp = dict()
    for ch in p:
        if dicp.get(ch)==None:
            dicp[ch]=1
        else:
            dicp[ch] += 1

    dics = dict()
    for ch in s[:right+1]:
        if dics.get(ch)==None:
            dics[ch]=1
        else:
            dics[ch] += 1

    while right<len(s):
        if dicp == dics:
            res.append(left)
            # This position of sliding window does not contain Anagram.
        if right+1<len(s):
            # print(left, dics)
            dics[s[left]] -= 1
            if dics[s[left]]==0:
                del dics[s[left]]
            left += 1
            right += 1

            if dics.get(s[right])==None:
                dics[s[right]]=1
            else:
                dics[s[right]] += 1
        else:
            break

    return res

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))










