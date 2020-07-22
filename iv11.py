class Solution:
    def minArray(self, numbers: list) -> int:
        n = len(numbers)
        for i in range(n-1, 0, -1):
            if numbers[i-1]>numbers[i]:
                return numbers[i]
        return numbers[0]
