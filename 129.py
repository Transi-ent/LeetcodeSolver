# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        1, 先求出每条二叉树路径上的数字，递归；
        2，将所有的数字相加；
        :param root:
        :return:
        """
        if root is None:
            return 0

        lyst = []
        lyst = self._sumNumbers(root, lyst, 0)
        return sum(lyst)

    def _sumNumbers(self, root: TreeNode, lyst: list, num: int) -> list:

        if root is None:
            return lyst

        num = 10 * num + root.val
        if root.left is None and root.right is None:
            # num = 10 * num + root.val
            lyst.append(num)
            return lyst
        else:

            self._sumNumbers(root.left, lyst, num)
            self._sumNumbers(root.right, lyst, num)
            return lyst

