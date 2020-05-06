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

class Solution2:
    """
    仅需验证 BST 的有序性即可，即验证当前节点与其左右子节点的关系
    """
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.onLeft(root.left, root.val) and\
               self.onRight(root.right, root.val) and\
               self.isValidBST(root.left) and \
               self.isValidBST(root.right)

        # 验证左子节点
    def onLeft(self, left: TreeNode, pVal: int)-> bool:
        if left is None:
            return True
        return left.val < pVal and\
               self.onLeft(left.left, pVal) and\
               self.onLeft(left.right, pVal)

    def onRight(self, right: TreeNode, pVal: int) -> bool:
        if right is None:
            return True
        return pVal < right.val and\
               self.onRight(right.left, pVal) and\
               self.onRight(right.right, pVal)
