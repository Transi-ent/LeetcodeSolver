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
            tmp = [] # list of level value
            nodes = [] # list of next layer nodes
            while q:
                root = q.pop(0)
                tmp.append(root.val)
                if root.left: nodes.append(root.left)
                if root.right: nodes.append(root.right)

            q = nodes
            res.append(tmp)
        return res
