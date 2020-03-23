# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        return self.inorder(root, res)

    def inorder(self, root: TreeNode, lyst: list):
        #TODO: Python 中的列表是引用传递，你将列表传给一个函数，传的是该列表的引用
        #TODO：..在函数中对该列表进行修改时，原列表也会变化。

        if root is None:
            return []

        self.inorder(root.left, lyst)

        lyst.append(root.val)

        self.inorder(root.right, lyst)

        return lyst

    def inorderTraversal(self, root: TreeNode) -> list:

        if root is None:
            return []

        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node is not None:

                if node.right is not None:
                    stack.append(node.right)

                stack.append(node.val)

                if node.left is not None:
                    stack.append(node.left)

        return res

