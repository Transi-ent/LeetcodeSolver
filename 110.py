# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if root is None:
            return True

        if abs(self.getHeight(root.left)-self.getHeight(root.right))<2 and \
            self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

        return False

    def getHeight(self, root: TreeNode):

        if root is None:
            return 0

        return max(self.getHeight(root.left),
                   self.getHeight(root.right))+1

    def isBalanced2(self, root: TreeNode) -> bool:

        if root is None:
            return True

        return abs( self.height(root.left) - self.height(root.right) ) <= 1 and \
    self.isBalanced2(root.left) and self.isBalanced2(root.right)

    def height(self, root: TreeNode):
        if root is None:
            return 0

        return max( self.height(root.left), self.height(root.right) ) + 1
