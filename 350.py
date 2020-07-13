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

class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        dic = {}
        for em in nums1:
            dic[em] = dic.get(em, 0) + 1

        res = []
        for em in nums2:
            if em in dic:
                res.append(em)
                dic[em] -= 1
                if dic[em]==0:
                    del dic[em]

        return res

print(Solution().intersect([1,2,2,1], [2,2]))
