# 给定一个数组，找出这个数组中最短连续子数组使得该子数组的和大于s

def minSubarrayLen(nums, target):

    left, right, n, res = 0, 0, len(nums), -1   # [left ... right] to store the sum of subarray

    sums = [nums[0]]*n

    for i in range(1, n):
        sums[i] = sums[i-1]+nums[i]

    while right<n:

        if (left==0 and sums[right]<target) or (sums[right]-sums[left-1]<target):

            right+=1

        else:
            if right+1-left<res:
                res=right+1-left

            left+=1

    return res


def minSubarrayLen2(nums, target):

    l, r, res, sum = 0, -1, -1, float('-inf')

    while l<len(nums):

        if r+1<len(nums) and sum<target:
            r +=1
            sum+=nums[r]


        else:
            sum -=nums[l]
            l+=1

        if sum>=target:
            res = min(res, r+1-l)

    return res


def minSubArrayLen( s: int, nums: list) -> int:
    """
    1,使用滑动窗口技术，使用两个指针分别指向窗口的两个左右边界;
    2,初始时，两个指针都位于数组的 0 索引位置；
    3,在滑动窗口滑动过程中，窗口区间内元素之和满足条件，则左边界右滑，不满足条件，则右边界右滑；
    4,可以通过记录区间和进行优化，即记录窗口区间内所有元素的和，
      ..右边界右滑，则加上新加入的元素，左边界右滑，则减去新滑出的元素；
    窗口区间： [left, right]
    :param s:
    :param nums:
    :return:
    """
    if sum(nums)<s:
        return 0

    minLen = len(nums)
    left, right = 0, 0
    sum_tmp = nums[0]
    while right<len(nums):
        # sum_tmp = sum(nums[left: right+1])
        if sum_tmp >= s:
            if right-left+1<minLen:
                minLen = right - left + 1
            sum_tmp -= nums[left]
            left += 1

        else:
            right += 1
            if right<len(nums):
                sum_tmp += nums[right]


    return minLen

a = minSubArrayLen(7, [2,3,1,2,4,3])

print(a)

