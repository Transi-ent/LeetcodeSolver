def fourSum( nums: list, target: int) -> list:
    """
    依然使用查找表的思路，查找表的Key值为两个元素之和，Value值为取得该sum值的
    ...两个元素的索引组成的元组。
    :param nums:
    :param target:
    :return:
    """
    d, res = {}, []

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            another = target - (nums[i] + nums[j])
            if d.get(another) and i!=d[another][0] and j!=d[another][1]:
                res.append( d[another][2:]+[nums[i], nums[j]] )
                d[nums[i]+nums[j]] = [i, j, nums[i], nums[j]]
            else:
                d[nums[i]+nums[j]] = [i, j, nums[i], nums[j]]

    res = [list(i) for i in res]
    return res

print(fourSum([1,0,-1,0,-2,2], 0))
