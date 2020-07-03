# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if root is None:
            return []
        res = []
        q = [root]

        while q:
            root = q.pop(0)
            res.append(root.val)
            if root.left: q.append(root.left)
            if root.right: q.append(root.right)

        return res
