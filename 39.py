class Solution:
    """
    回溯法。枝叶粗大，
    """
    def combinationSum(self, candidates: list, target: int) -> list:
        s = set()
        res = self.findCombnt(candidates, target, 0, [],[],s)
        print(res)
        return res

    def findCombnt(self, nums: list, target: int, index: int,
                   tmplist: list, res: list, s: set) ->list:
        n = len(nums)
        if index>=n:
            return res

        for i in range(index, n):
            copyOftmp = tmplist.copy()
            copyOfs = s.copy()
            sumVal = sum(copyOftmp)
            if sumVal+nums[i]==target:
                tmp = copyOftmp+[nums[i]]
                tmp.sort()

                ss = ''.join([str(i) for i in tmp])
                if not ss in s:
                    res.append(copyOftmp+[nums[i]])
                    s.add(ss)
            elif sumVal+nums[i]>target:
                self.findCombnt(nums, target, index+1, copyOftmp, res, s)
            else:
                self.findCombnt(nums, target, index, copyOftmp+[nums[i]], res, s)

        return res

class Solution2:
    """
    回溯法。改进版
    """
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []
        candidates.sort()
        n = len(candidates)
        def traceback(index: int, tmpsum: int, tmp: list):
            if tmpsum>target or index>=n:
                return
            if tmpsum==target:
                res.append(tmp)

            for i in range(index, n):
                if tmpsum+candidates[i]>target:
                    break # 因为已经排好序了，后面的元素只会越来越大
                # 回溯法的本质即为在一个循环中递归调用自身
                traceback(i, tmpsum+candidates[i], tmp+[candidates[i]])

        traceback(0, 0, [])
        print(res)
        return res

class Solution3:
    """
    递归。
    """
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []
        candidates.sort()
        n = len(candidates)
        def dfs(index: int, tmpsum: int, tmp: list):
            if tmpsum>target or index>=n:
                return
            if tmpsum==target:
                res.append(tmp)
                return

            dfs(index, tmpsum+candidates[index], tmp+[candidates[index]])
            dfs(index+1, tmpsum, tmp)

        dfs(0, 0, [])
        print(res)
        return res




Solution3().combinationSum([2,3,6,7], 7)
