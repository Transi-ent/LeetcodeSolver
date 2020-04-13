# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        root = None
        if preorder:
            rv = preorder[0]
            rootIdx = inorder.index(rv)

            root = TreeNode(rv)
            root.left = self.buildTree(preorder[1:1+rootIdx], inorder[:rootIdx])
            root.right = self.buildTree(preorder[1+rootIdx:], inorder[rootIdx+1:])
        else:
            return root

        return root
