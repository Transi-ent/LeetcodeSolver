class Solution:

    def merge(self, intervals: list) -> list:
        n = len(intervals)
        if n<2:
            return intervals

        intervals.sort(key=lambda x: x[0])
        res = []
        curItv = intervals.pop(0)
        while intervals:
            itv = intervals.pop(0)
            # 该区间处于包含状态
            if itv[1]<=curItv[1]:
                continue
            # 处于交集状态
            elif itv[0]<=curItv[1]:
                curItv[:] = [curItv[0], itv[1]]
            # 两交集相离
            else:
                res.append(curItv)
                curItv = itv
        res.append(curItv)
        print(res)
        return res

Solution().merge(
    [
        #[1,3],[2,6],[8,10],[15,18]
        [1,4],[4,5]
    ]
)
