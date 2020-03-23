# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        if root is None:
            return True

        return self.onLeft(root.left, root.val) \
               and self.onRight(root.right, root.val) \
               and self.isValidBST(root.left) \
               and self.isValidBST(root.right)

    def onLeft(self, root: TreeNode, pval: int) -> bool:
        if root is None:
            return True

        return root.val<pval and self.onLeft(root.left, pval) \
            and self.onLeft(root.right, pval)

    def onRight(self, root: TreeNode, pval: int) -> bool:
        if root is None:
            return True

        return root.val>pval and self.onRight(root.left, pval) \
            and self.onRight(root.right, pval)
