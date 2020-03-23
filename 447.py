"""
回旋镖的数量
"""

def numberOfBoomerange(points: list):
    """
    给定一个点坐标数组，求出所有回旋镖组合；
    因为点 i 为枢纽点，求出其他所有点到点 i的距离di，在di下点的个数，只有di的个数大于
    1时，才存在回旋镖点。
    :param points:
    :return:
    """

    def dist(point1: list, point2: list):
        # 求两个点之间的距离
        return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2


    res = 0
    for i in range(len(points)):

        dmap = dict()

        for j in range(len(points)):

            if i!=j:
                dst = dist(points[i], points[j])
                if dmap.get(dst):
                    dmap[dst]+=1

                else:
                    dmap[dst] = 1

        for v in dmap.values():
            if v>1:
                res += v*(v-1)

    return res


def numberOfBoomerangs(self, points: list) -> int:
    def dist(p1: list, p2: list):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    res = 0
    for i, pm in enumerate(points):

        d_dist = {}
        # Get all the distance from pivot point to other points, and
        # .. put them into a map,
        for j, ps in enumerate(points):
            if i != j:
                d_tmp = dist(pm, ps)
                d_dist[d_tmp] = d_dist.get(d_tmp, 0) + 1

        res += sum([v*(v-1) for v in d_dist.values() if v>1])


    return res

