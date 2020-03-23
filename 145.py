# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        res = []
        return self.postorder(root, res)


    def postorder(self, root: TreeNode, lyst: list):
        if root is None:
            return []

        self.postorder(root.left, lyst)


        self.postorder(root.right, lyst)


        lyst.append(root.val)

        return lyst

