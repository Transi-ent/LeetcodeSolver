# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        # 判断两棵二叉树在结构上以及每一个节点上的取值是否一样
        if (p is None and q is not None) or (q is None and p is not None):
            return False

        if p is None and q is None:
            return True

        return p.val == q.val and self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
