# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    可以分为 2 种情况：
    1、两个树相同；
    2、t 出现在 s 的左子树或右子树；
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        return self.sameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s: TreeNode, t: TreeNode)->bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
