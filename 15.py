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

class Solution:
    """
    使用查找表，并将找到的结果排好序连成一个字符串放入哈希集合中
    形成一个唯一性标识去重。
    超时！！！
    """
    def threeSum(self, nums: list) -> list:
        n = len(nums)
        if n<3:
            return []
        map = {}
        res,s = [], set()
        for i, e in enumerate(nums):
            if map.get(e):
                map[e].append(i)
            else:
                map[e]=[i]

        for i in range(0, n-2):
            for j in range(i+1, n-1):
                tmp = nums[i] + nums[j]
                print("i={}, j={}, n={}".format(i,j,n))
                if i==0 and j==2:
                    print("tmp: {}".format(tmp))

                if map.get(-tmp):
                    lyst = map.get(-tmp)
                    for k in lyst:
                        if k>j:
                            tmp = [nums[i],nums[j],nums[k]]
                            ts = ''.join([str(t) for t in sorted(tmp)])
                            if not ts in s:
                                res.append(tmp)
                                s.add(ts)

        print(res)
        return res

class Solution2:
    def threeSum(self, nums: list) -> list:
        n = len(nums)
        if n<3:
            return []
        if all([i==0 for i in nums]):
            return [[0,0,0]]
        map = {}
        res,s = [], set()
        nums.sort()
        for i, e in enumerate(nums):
            if map.get(e):
                map[e].append(i)
            else:
                map[e]=[i]

        for i in range(0, n-2):
            for j in range(i+1, n-1):
                tmp = nums[i] + nums[j]
                print("i={}, j={}, n={}".format(i,j,n))
                if i==0 and j==2:
                    print("tmp: {}".format(tmp))

                if map.get(-tmp):
                    lyst = map.get(-tmp)
                    for k in lyst:
                        if k>j:
                            tmp = [nums[i],nums[j],nums[k]]
                            ts = ''.join([str(t) for t in tmp])
                            if not ts in s:
                                res.append(tmp)
                                s.add(ts)

        print(res)
        return res

Solution2().threeSum([-1,0,1,2,-1,-4])
