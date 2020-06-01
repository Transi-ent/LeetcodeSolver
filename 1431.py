class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        MAX = max(candies)
        return [i+extraCandies>=MAX for i in candies]
