class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n<1:
            return 0
        m -= 1
        lyst = [i for i in range(n)]
        li = 0
        while len(lyst)>1:

            lyst.pop((m+li)%len(lyst))
            li = (m+li)%(len(lyst)+1)
        #   print("lyst: {}".format(lyst))
        return lyst.pop()

Solution().lastRemaining(10, 17)
