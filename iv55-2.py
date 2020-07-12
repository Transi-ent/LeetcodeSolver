# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode):
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1
        if root is None:
            return True
        if abs(height(root.left)-height(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
