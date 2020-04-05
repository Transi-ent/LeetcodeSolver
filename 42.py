class Solution:
    """
    每个坑能够存多少水，取决于取决于 pit 边上第二大的值，
    求出该值与区间的每一个值的差之和
    """
    def trap(self, height: list) -> int:
        maxh = max(height)
        mhi = height.index(maxh)
        return self.findPit(height, mhi, True)+self.findPit(height, mhi, False)


    def findPit(self, height: list, hi: int, toLeft: bool ) ->int:
        """
        已知最大值的索引，找到距离最大值最近的一个 pit，
        """
        if hi<=0 or hi>=len(height)-1:
            return 0
        res = 0
        if toLeft:
            maxh = max(height[:hi])
            mhi = height[:hi].index(maxh)
            res = sum( [maxh - i for i in height[mhi+1: hi]] )
            res += self.findPit(height, mhi, True)
        else:
            maxh = max(height[hi+1:])
            mhi = height[hi+1:].index(maxh)
            res = sum([maxh - i for i in height[hi + 1: mhi]])
            res += self.findPit(height, mhi, False)
        print(res)
        return res

class Solution2:
    """
    按水的高度求出总雨水量
    """
    def trap(self, height: list) -> int:
        if len(height)<3:
            return 0
        mh = max( height )
        SUM = 0
        for h in range(1, mh+1):
            tmp_sum = 0
            start = False
            for i in range(len(height)):
                if start and height[i]<h:
                    tmp_sum += 1

                if height[i]>=h:
                    SUM += tmp_sum
                    tmp_sum = 0
                    start = True
        return SUM


res = Solution().trap([2, 0, 2])
print(res)
