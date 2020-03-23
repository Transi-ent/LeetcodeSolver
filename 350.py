def intersect(nums1: list, nums2: list) -> list:

    dict2, res = dict(), []
    # static frequency of all elements
    for n in nums2:
        if dict2.get(n)==None:
            dict2[n] = 1
        else:
            dict2[n] += 1

    for n in nums1:
        if n in dict2 and dict2[n]>0:
            res.append(n)
            dict2[n] -= 1

    return res
