"""
给定一个整型数组，找出所有的3元组，使元组和为0
"""

def threeSum(nums: list, target: int):

    d = dict()

    for i in range(len(nums)-1):

        for j in range(i, len(nums)):

            complement = -(nums[i]+nums[j])

            if d.get(complement):
                return [complement, nums[i], nums[j]]


            d[complement] = 1

def threeSum( nums: list) -> list[list[int]]:
    """
    As there are 3 numbers, even we use findTable, 2 for-loop
    ..are still needed.
    :param nums:
    :return:
    """
    d, res = {}, []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)):
            tmp = -(nums[i] + nums[j])
            if d.get(tmp) and d[tmp]!=j:
                res.append([nums[i], nums[j], tmp])

            else:
                d[nums[j]] = j

    return res

