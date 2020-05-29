class Solution:
    """
    暴力解，三层 for 循环
    """
    def threeSumClosest(self, nums: list, target: int) -> int:
        if len(nums)<3:
            return None

        dic = {}
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):

                    dic[(i, j, k)] = nums[i]+nums[j]+nums[k]

        res = float("-inf")
        for k, v in dic.items():
            if abs( res - target ) > abs( v - target ):
                res = v
        return res

class Solution2:
    """
    两层 for 循环，运算时间不减反增
    """
    def threeSumClosest(self, nums: list, target: int) -> int:
        if len(nums)<3:
            return None

        dic = {}
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                dic[(i, j)] = nums[i]+nums[j]

        res = float("-inf")
        for i in range(len(nums)):
            for k, v in dic.items():
                if not i in k:
                    tmp = v + nums[i]
                    if abs(res - target)>abs(tmp - target):
                        res = tmp
        return res

class Solution3:
    """
    先对数组排序，然后对排完序的数组用双指针操作，求最接近的三数之和；
    对于一个涉及到数组的问题，输出结果与数组元素的位置无关且暴力解复杂度较大时，可先排序再搜索
    """
    def threeSumClosest(self, nums: list, target: int) -> int:
        n = len(nums)
        nums.sort()
        res = float('-inf')
        for i in range(n-2):
            mid = i + 1
            right = n - 1
            while mid<right:
                tmpSum = nums[i] + nums[mid] + nums[right]
                if abs(tmpSum-target)<abs(res-target):
                     res = tmpSum

                if tmpSum==target:
                    return tmpSum
                elif tmpSum<target:
                    mid += 1
                else:
                    right -= 1

        return res








