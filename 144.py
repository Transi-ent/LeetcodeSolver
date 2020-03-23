class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_:
    def preorderTraversal_(self, root: TreeNode) -> list:
        # lyst = []
        # return self.preorder(root, lyst)
        pass

    def preorder(self, root: TreeNode, lyst: list):
        #
        # if not root:
        #     return
        #
        # lyst.append(root.val)
        # lyst += self.preorder(root.left, lyst)
        # lyst += self.preorder(root.right, lyst)
        #
        # return lyst
        pass

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:

        if root is None:
            return []

        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)

                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)

        return res

    def preorderTraversal2(self, root: TreeNode) -> list:
        res = []
        return self.preorder(root, res)


    def preorder(self, root: TreeNode, lyst: list):
        if root is None:
            return

        lyst.append(root.val)
        self.preorder(root.left, lyst)
        self.preorder(root.right, lyst)

        return lyst


















