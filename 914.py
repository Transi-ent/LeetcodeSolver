from math import gcd
from fractions import gcd
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

class Solution2:
    """
    求出每张牌点数出现的频次，求出频次数组的最大公因数；
    求一个数组所有元素最大公因数的方法：已知数组 arr, 先求出 arr[:2] 的最大公因数，再将该 公因数依次与
    arr[2: ]余下元素依次代入求公因数，最后的公因数即为整个数组最大的公因数。
    TODO： 求最大公因数方法 --- 「辗转相除法」
    """
    def hasGroupsSizeX(self, deck: list) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count_map = {}
        for num in deck:
            count_map[num] = count_map.get(num, 0) + 1
        pre_val = None
        for val in count_map.values():
            if not pre_val:
                pre_val = val
            else:
                pre_val = gcd(pre_val, val)
                if pre_val == 1:
                    return False
        return pre_val != 1
