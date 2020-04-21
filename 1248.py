class Solution:
    """
    暴力解，超出时间限制
    """
    def numberOfSubarrays(self, nums: list, k: int) -> int:
        nums = [i%2 for i in nums]

        SUM = sum(nums)
        if SUM<k:
            return 0

        n = len(nums)
        res = 0
        for i in range(n-k+1):
            tmpSum = sum(nums[i:i+k])
            for j in range(i+k-1, n):
                if j!=i+k-1:
                    tmpSum += nums[j]

                if tmpSum==k:
                    res += 1
                elif tmpSum>k:
                    break

        print(res)
        return res

class Solution2:
    """
    记录奇数出现时所在的索引位置，使用数学法计算。
    若已知第 i 个奇数，以及第 i+k-1 个奇数的位置，且已知第 i 个奇数与其上一个奇数
    的索引相隔为 m, 第 i+k-1 个奇数与其下一个奇数的索引相隔为 n, 则该区间有
    (m+1)*(n+1) 个子区间
    """
    def numberOfSubarrays(self, nums: list, k: int) -> int:
        idx = []
        for i, num in enumerate(nums):
            if num&1==1:
                idx.append(i)

        n = len(idx)
        if n<k:
            return 0
        res = 0
        left, right = 0, -1
        cnt = 0
        # idx = [-1] + idx + [n]
        while right<n:

            if cnt<k:
                right += 1
                cnt += 1
            elif cnt==k:
                mc, nc=0, 0
                if left>0:
                    mc = idx[left]-idx[left-1]-1
                elif left==0 and idx[left]>0:
                    mc = idx[left]
                if right<n-1:
                    nc = idx[right+1]-idx[right]-1
                elif right==n-1 and idx[right]<len(nums)-1:
                    nc = len(nums) - idx[right] - 1
                print("right:{}, n:{}".format(right, n))
                print("mc:{}, nc:{}".format(mc, nc))
                res += (mc+1)*(nc+1)
                left += 1
                right += 1
        print(res)
        return res


Solution2().numberOfSubarrays([1,1,2,1,1], 3)
