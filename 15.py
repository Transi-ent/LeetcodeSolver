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

class Solution3:
    """
    1、暴力解：三层for循环；
    2、查找表：将所有元素放入查找表内，两层for循环+一个查找表，时间复杂度O(n^2)
    """
    def threeSum(self, nums: list) -> list:
        if len(nums)<3:
            return []

        # 建立查找表
        map = {}
        for i, num in enumerate(nums):
            if map.get(num):
                map[num].append(i)
            else:
                map[num] = [i]

        res = []
        visited = set()
        print(map)
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):

                third = 0 - nums[i] - nums[j]

                if third in map:
                    print("third : {}".format(third))
                    tmp = [nums[i], nums[j]]
                    idxs = map[third]
                    idxs = [k for k in idxs if k > j]
                    while idxs:
                        print("idxs : {}".format(idxs))
                        copyOfList = tmp.copy()
                        copyOfList.append(nums[idxs.pop(0)])
                        s = ''.join([str(w) for w in sorted(copyOfList)])
                        if not s in visited:
                            print("copy : {}".format(copyOfList))
                            res.append(copyOfList)
                            visited.add(s)

        return res

res = Solution3().threeSum([-1,0,1,2,-1,-4])
print(res)
