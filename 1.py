"""
给定一个数组nums，返回两个索引值i和j，使得 nums[i]+nums[j]等于
给定的 target 值。
"""

# 1，暴力解，两层 for 循环

# 2, 查找表

def twoSum(nums: list, target: int):

    d = dict()
    res = []
    for i  in range(len(nums)):

        d[nums[i]] = target-nums[i]

        if d.get(target-nums[i]):
            res.extend([nums.index(target-nums[i]), i])

            break

    return res


def twoSum2(nums: list, target: int):

    d = dict() # [key--num: value--index]

    for i in range(len(nums)):

        tmp = target-nums[i]

        if d.get(tmp):

            return [d[tmp], i]

        d[nums[i]] = i

    assert False, " wrong input"

def twoSum3( nums: list, target: int) -> list:
    d = {}
    for i, e in enumerate(nums):
        d[e] = i

    for i, e in enumerate(nums):
        another = target - e
        if d.get(another) and i!=d[another]:
            return [i, d[another]]













