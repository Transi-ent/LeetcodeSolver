class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        return self.merge(t1, t2, TreeNode(0))

    def merge(self, t1: TreeNode, t2: TreeNode, root: TreeNode):
        if t1 is None and t2 is None:
            return None
        if t1 is None and t2 is not None:
            return t2
        if t1 is not None and t2 is None:
            return t1
        root = TreeNode(0)

        root.left = self.merge(t1.left, t2.left, root.left)

        root.right = self.merge(t1.right, t2.right, root.right)

        root.val = t1.val + t2.val

        return root

class Solution2:
    """
    简化版，在所给的树上直接修改
    """
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            t1.val += t2.val
            return t1
        return t1 or t2














