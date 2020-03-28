class Solution:
    """
    在每加入一个新的单词之前，都先判断下 words[i] 是不是 words[i-1] 的前缀
    """
    def minimumLengthEncoding(self, words: list) -> int:
        s = set(words)
        for word in words:
            for i in range(1, len(word)):
                s.discard(word[i:])
        res = 0
        for em in s:
            res += len(em) + 1
        return res
