# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self._isSymmetric1(root.left, root.right)

    def _isSymmetric1(self, p: TreeNode, q: TreeNode):

        if (p is None and q is not None) or \
                (p is not None and q is None):
            return False

        if p is None and q is None:
            return True

        return p.val==q.val and self._isSymmetric1(p.left, q.right) and \
            self._isSymmetric1(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is None or root.right is None or root.left.val\
                != root.right.val:
            return False

        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left: TreeNode, right: TreeNode):

        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return left.val==right.val and self._isSymmetric(left.left, right.right)\
            and self._isSymmetric(left.right, right.left)

