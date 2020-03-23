def maxPoints(points: list) -> int:
    """
    每次选取一个点，选取过该固定点的直线，只要斜率相同，这些点就在同一条直线上
    :param points:
    :return:
    """
    def slope(p1: list, p2: list):
        # Get the slope of a line.
        if p2[1] - p1[1] != 0:
            return (p2[0] - p1[0]) / (p2[1] - p1[1])
        elif p2[0] - p1[0] != 0 and p2[1] - p1[1] == 0:
            return 'inf'
        elif p2[0] - p1[0] == 0 and p2[1] - p1[1] == 0:
            return 'same'
    n = len(points)
    if n>2:
        res = 0
        for i, pf in enumerate(points):
            d = {}
            samePoint = 0
            print("Point: ", pf)
            for j, p in enumerate(points):
                if i != j:

                    k = slope(pf, p)
                    print('    ',k, end=', ')
                    if k != 'same':
                        d[k] = d.get(k, 0) + 1
                    else:
                        samePoint += 1
            print()
            if len(d)!=0:
                tmp = max(d.values()) + samePoint
            else:
                tmp = samePoint
            res = max(res, tmp)

        return res+1
    else:
        return n

print(maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))
