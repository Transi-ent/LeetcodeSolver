class Solution:
    def majorityElement(self, nums: list) -> int:
        n = len(nums)
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num]>n//2:
                return num

print(Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
