# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(left: TreeNode, right: TreeNode)->bool:

            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            return left.val==right.val and isSym(left.left, right.right) and \
                   isSym(left.right, right.left)

        if root is None:
            return True

        return isSym(root.left, root.right)
