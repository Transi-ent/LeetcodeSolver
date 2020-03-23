# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth1(self, root: TreeNode) -> int:
        #
        # def _minDepth( root: TreeNode) -> int:
        #
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None or root.right is None:
            return max(self.minDepth(root.left), self.minDepth(root.right))+1

        return min(self.minDepth(root.left), self.minDepth(root.right))+1


    def minDepth2(self, root: TreeNode) -> int:

        if root is None:
            return 0

        return self._minDepth2(root)

    def _minDepth2(self, root: TreeNode):

        if root and root.left is None and root.right is None:
            return 1

        if root.left and not root.right:
            return self._minDepth2(root.left) + 1

        if not root.left and root.right:
            return self._minDepth2(root.right) + 1

        if root.left and root.right:
            return min( self._minDepth2(root.left), self._minDepth2(root.right) )+1















