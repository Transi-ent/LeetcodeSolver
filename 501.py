# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> list:
        dic = dict()
        self._findMore(root, dic)
        # 已经统计出了词频，现在找出众数
        tmp, ret = 0, []
        for v in dic.values():
            if v >tmp:
                tmp=v

        for k, v in dic.items():
            if v==tmp:
                ret.append(k)

        return ret

    def _findMore(self, root: TreeNode, dic: dict):

        # 考虑递归到底的情况
        if root is None:
            return

        # 此时root不为null, 统计该节点值
        if dic.get(root.val) is None:
            dic[root.val] = 1
        else:
            dic[root.val] += 1

        # 继续递归
        self._findMore(root.left, dic)
        self._findMore(root.right, dic)
