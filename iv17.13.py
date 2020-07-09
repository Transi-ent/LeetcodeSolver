import functools
class Solution:
    def respace(self, dictionary: list, sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w)!=-1}
        lens = [len(w) for w in dictionary]
        lens.sort()
        N, res = len(sentence), 0
        @functools.lru_cache(maxsize=1000)
        def search(i: int)->int:# 从 Sentence的索引 i 位置开始搜索使得在字典中未出现字符最少的字符数
            # 当字符串为空时，返回0
            if i>=N: return 0

            lyst = []
            # 从索引为 i 的字符开始，搜索所有接下来可能为单词的子树
            lyst = [search(i+l) for l in lens if i+l<=N and sentence[i: i+l] in dictionary]
            # 从索引为 i 的字符开始，接下来的字符并未在字典中出现过
            lyst += [1+search(i+1)]
            return min(lyst) if lyst else 0

        return search(0)

dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
print(Solution().respace(dictionary, sentence))
