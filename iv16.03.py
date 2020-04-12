class Solution:
    def intersection(self,
                     start1: list,
                     end1: list,
                     start2: list,
                     end2: list) -> list:
        d = 1E-6 # 用于排查浮点误差
        # 求斜率
        k1, k2 = None, None
        if start1[0]!=end1[0]:
            k1 = (end1[1]-start1[1])/(end1[0]-start1[0])
        else:
            k1 = float('inf')

        if start2[0]!=end2[0]:
            k2 = (end2[1]-start2[1])/(end2[0]-start2[0])
        else:
            k2 = float('inf')
        # 当2直线平行时
        if k1==k2:
            x1, x2, x3, x4 = start1[0], end1[0], start2[0], end2[0]
            y1, y2, y3, y4 = start1[1], end1[1], start2[1], end2[1]
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            if x3 > x4:
                x3, x4 = x4, x3
                y3, y4 = y4, y3
            # 当2直线重合时
            if k1*(start2[0]-start1[0]) + start1[1]==start2[1] or \
                    (k1==float('inf') and end1[0]==end2[0]):
                if k1 == float('inf'):
                    if max(start1[1], end1[1]) >= min(start2[1], end2[1]) and \
                            max(start2[1], end2[1]) >= min(start1[1], end1[1]):
                        if y1 > y2:
                            y1, y2 = y2, y1
                        if y3 > y4:
                            y3, y4 = y4, y3
                        if y3 <= y2 <= y4:
                            return [x3, y3]
                        elif y3<=y1<=y4:
                            return [x1, y1]
                    else:
                        return []
                if x2<x3 or x4<x1:
                    return []
                else:
                    if x3<=x1<=x4:
                        return [x1, y1]
                    else:
                        return [x3, y3]
            # 当2直线平行且不重合时
            else:
                return []
        # 当2直线不相互平行且都不与 y 轴平行时
        if k1!=float('inf') and k2!=float('inf'):
            x = (start2[1] - start1[1] + k1*start1[0] - k2*start2[0])/(k1 - k2)
            y = k1*(x - start1[0]) + start1[1]
            print("x: {}, y: {}".format(x,y))
            x1, x2, x3, x4 = start1[0], end1[0], start2[0], end2[0]
            y1, y2, y3, y4 = start1[1], end1[1], start2[1], end2[1]
            if x1>x2:
                x1, x2 = x2, x1
            if x3>x4:
                x3, x4 = x4, x3
            if y1>y2:
                y1, y2 = y2, y1
            if y3>y4:
                y3, y4 = y4, y3
            if x1-d<=x<=x2+d and x3-d<=x<=x4+d and y1-d<=y<=y2+d and y3-d<=y<=y4+d:
                return [x, y]
            else:
                return []
        else:
            # 当这两条直线中有一条平行于 y 轴, 且两直线不平行
            if k1==float('inf'):
                x = end1[0]
                y = k2*(x - start2[0]) + start2[1]
                if y<min(start1[1], end1[1]) or y>max(start1[1], end1[1]):
                    return []
                else:
                    return [x, y]
            elif k2==float('inf'):
                x = end2[0]
                y = k1 * (x - start1[0]) + start1[1]
                if y < min(start2[1], end2[1]) or y > max(start2[1], end2[1]):
                    return []
                else:
                    return [x, y]


p = Solution().intersection([12,-55],
[59,-60],
[4,-55],
[81,-62])
print(p)
