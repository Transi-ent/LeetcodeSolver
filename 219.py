"""
给定一个整形数组nums 和一个整数 k, 是否存在索引i 和 j,
使得 nums[i]==nums[j]，且i, j 之差不大于k
"""

def containDuplicate(nums: list, k):

    l, r = 0, -1 # [l ... r] 滑动窗口范围

    s = set()

    while r<len(nums):

        if r+1<len(nums) and r+1-l<k:
            r+=1
            tmp = nums[r]
            if s.__contains__(tmp):
                return True

            s.add(tmp)

        else:
            s.remove(nums[l])
            l+=1

    return False



def containsNearbyDuplicate( nums: list, k: int) -> bool:
    """
    Sliding Window + Find Table
    :param nums:
    :param k:
    :return:
    """
    left, right, s = 0, 0, set()
    while right<len(nums):
        if nums[right] in s:
            return True
        else:
            s.add(nums[right])

        if right - left < k:
            right += 1
        else:
            s.remove(nums[left])
            left += 1
            right += 1

    return False

print(containsNearbyDuplicate([1,2,3,1], 3))
