class Solution:
    def findRepeatNumber(self, nums: list) -> int:
        map = {}
        for n in nums:
            if map.get(n):
                return n
            else:
                map[n] = 1
