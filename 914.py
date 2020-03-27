
class Solution:
    """
    统计每个点数的牌出现的频次，只要所有点数的牌存在一个大于等于2的公约数，
    ... 即可返回 TRUE，否则返回 False。
    """
    def hasGroupsSizeX(self, deck: list) -> bool:
        if len(deck)<2:
            return False
        map = {}
        for em in deck:
            map[em] = map.get(em, 0) + 1
        # n = len(deck)
        # m = len(map)
        vals = list(map.values())
        minV = min(map.values())
        # res, flag = False, False
        for i in range(2, minV+1):
            if all([v%i==0 for v in vals]):
                return True
        return False
