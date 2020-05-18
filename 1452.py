class Solution:
    def peopleIndexes(self, favoriteCompanies: list) -> list:
        map = {}
        for i, lyst in enumerate(favoriteCompanies):
            map[i] = set(lyst)

        res = []
        for i, lyst in enumerate(favoriteCompanies):
            isSub = False
            for k, v in map.items():
                if k!=i:
                    if set(lyst).issubset(v):
                        isSub = True
                        break
            if not isSub:
                res.append(i)

        return res


class Solution2:
    """
    利用 Python 特性的简化写法
    """
    def peopleIndexes(self, f: list) -> list:
        f = [set(x) for x in f]
        index = [ sum(x&y==x for y in f)<2 for x in f]
        return [i for i in range(len(f)) if index[i]]
