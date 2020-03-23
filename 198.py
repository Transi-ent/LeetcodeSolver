class Solution:
    """
    使用回溯法，即遍历所有情况，从头开始，每种情况都搜索到底（DFS），
    搜索到底后再返回从最近一个分支继续搜索；
    Exceed time limit！
    """
    def rob(self, nums: list) -> int:
        return self.tryRob(nums, 0)
    def tryRob(self, nums: list, index: int) -> int:
        # 考虑抢劫 nums[index ... n] 范围内的住户
        n = len(nums)
        if index >= n:
            return 0
        res = 0
        for i in range(index, n):
            res = max(res, nums[i]+self.tryRob(nums, i+2))
        return res

class Solution2:
    """
    记忆化搜索：在上述方法的基础之上，记录每一个计算过的子问题的计算结果。
    递归的过程中生成一颗递归搜索树，该树存在着重复子问题枝干
    """
    def rob(self, nums: list) -> int:
        memo = [-1] * len(nums)
        return self.tryRob(memo, nums, 0)
    def tryRob(self,memo: list, nums: list, index: int) -> int:
        # 考虑抢劫 nums[index ... n] 范围内的住户
        n = len(nums)
        if index >= n:
            return 0
        if memo[index]!=-1:
            return memo[index]
        res = 0
        for i in range(index, n):
            res = max(res, nums[i]+self.tryRob(memo, nums, i+2))

        memo[index] = res
        return res
