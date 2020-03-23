def intersection(nums1: list, nums2: list) -> list:

    set1 = set(nums1)
    #set2 = set(nums2)
    res = set()

    for num in nums2:
        if num in set1:
            res.add(num)

    return list(res)
