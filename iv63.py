class Solution:
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n<2:
            return 0
        benefit, MIN, res = False, prices[0], 0
        for i in range(1, n):
            if prices[i]<MIN:
                MIN = prices[i]

            res = max(res, prices[i]-MIN)

        return res

print(Solution().maxProfit([7,6,4,3,1]))
