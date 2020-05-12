class Solution:
    """
    暴力解—— 两层 for 循环
    """
    def maxProduct(self, nums: list) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            tmp = 1
            for j in range(i, len(nums)):

                tmp *= nums[j]
                res = max(res, tmp)
                print("[{}, {}], tmp_product={}".format(i, j, tmp))
        print(res)
        return res

class Solution2:
    """
    动态规划，记录当前最大值与全局最大值，因为最大值乘以负号会翻转，因此也需要记录最小值
    """
    def maxProduct(self, nums: list) -> int:
        MAX, imax, imin = float('-inf'), 1, 1
        for num in nums:
            if num<0:
                imax, imin = imin, imax

            imax = max(imax * num, num)
            imin = min(imin * num, num)

            MAX = max( imax, MAX )

        print(MAX)
        return MAX



Solution2().maxProduct([2,3,-2, 4])
