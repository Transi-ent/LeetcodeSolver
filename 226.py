# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree1(self, root: TreeNode) -> TreeNode:
        # 反转一个二叉树
        if root is None:
            return

        leftNode = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(leftNode)

        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:

        if root is None:
            return root

        left = root.left
        right = root.right

        root.left = self.invertTree2( right )
        root.right = self.invertTree2( left )

        return root
