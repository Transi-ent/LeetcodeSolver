class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices)<2:
            return 0

        return self.buySell(prices, 0)

    def buySell(self, prices: list, index: int) -> int:
        # 对 prices[index ... n] 内的股票进行处理
        n = len(prices)
        if index>=n or len(prices[index:])<2:
            return 0

        res = 0
        for i in range(index, n):
            res = max(res,)
