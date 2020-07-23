class Solution:
    def getLeastNumbers(self, arr: list, k: int) -> list:
        arr.sort()
        return arr[:k]

print(Solution().getLeastNumbers([3,2,1], 2))
