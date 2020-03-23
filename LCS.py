def longestCommonSequence(s1: str, s2: str) -> int:
    if s1=='' or s2=='':
        return 0

    if s1[-1]==s2[-1]:
        return longestCommonSequence(s1[:-1], s2[:-1])+1
    else:
        return max(
            longestCommonSequence(s1[:-1], s2),
            longestCommonSequence(s1, s2[:-1])
        )

def LCS(s1: str, s2: str) -> int:
    if s1=='' or s2=='':
        return 0
    memo = [[-1]*len(s2) for _ in range(len(s1))]
    return findLCS(s1, len(s1)-1, s2, len(s2)-1, memo)


def findLCS(s1: str, index1: int, s2: str, index2: int, memo: list) -> int:
    if index1<0 or index2<0:
        return 0

    if memo[index1][index2] != -1:
        return memo[index1][index2]

    res = 0
    if s1[index1] == s2[index2]:
        res = findLCS(s1, index1-1, s2, index2-1, memo) + 1
    else:
        res = max(
            findLCS(s1, index1-1, s2, index2, memo),
            findLCS(s1, index1, s2, index2-1, memo)
        )
    memo[index1][index2] = res
    return res
