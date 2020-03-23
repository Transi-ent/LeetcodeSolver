# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum1: int) -> list:
        """
        先把所有的路径都求出来，在将不符合要求的路径剔除出去
        :param root:
        :param sum:
        :return:
        """
        if root is None:
            return []

        lyst = []
        lyst = self._pathSum(root, lyst, '')
        lyst = [s[1:].split('.') for s in lyst]

        for i, lis in enumerate(lyst):
            lyst[i] = [int(em) for em in lis]

        return [e for e in lyst if sum(e)==sum1]

    def _pathSum(self, root: TreeNode, lyst: list, path: str) -> list:

        if root is None:
            return lyst

        if root.left is None and root.right is None:
            path += '.'
            path += str(root.val)
            lyst.append(path)
            return lyst
        else:
            path += '.'
            path += str(root.val)
            self._pathSum(root.left, lyst, path)
            self._pathSum(root.right, lyst, path)
            return lyst

