# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes1(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self._countNodes1(root, 1)

    def _countNodes1(self, root: TreeNode, n: int):

        if root is None:
            return 0

        if root.right is None and root.left is None:
            return n

        return max(self._countNodes1(root.left, 2*n),
                   self._countNodes1(root.right, 2*n+1))

    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self._countNodes(root)

    def _countNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return 1 + self._countNodes(root.left) + self._countNodes(root.right)

