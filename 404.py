# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        return self._sumOfLeftLeaves(root)

    def _sumOfLeftLeaves(self, root: TreeNode) -> int:

        if root is None:
            return 0

        if root.left is None and \
                root.right is None:
            return root.val

        if root.right is None or \
                (root.right.left is None and root.right.right is None):
            # 若不存在右子节点，或右子节点为叶子节点
            return self._sumOfLeftLeaves(root.left)

        return self._sumOfLeftLeaves(root.left)+\
               self._sumOfLeftLeaves(root.right)

    def sumOfLeftLeaves2(self, root: TreeNode) -> int:

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        return self._sumOfLeftLeaves2(root)

    def _sumOfLeftLeaves2(self, root: TreeNode):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        if root.left is None and root.right:
            return self._sumOfLeftLeaves2(root.right)

        if root.left  and root.right is None:
            if root.left.left is None and root.left.right is None:
                return root.left.val
            else:
                return self._sumOfLeftLeaves2(root.left)

        if root.left.left is None and root.left.right is None:
            return root.left.val + self._sumOfLeftLeaves2(root.right)
        else:
            return self._sumOfLeftLeaves2(root.left) + \
                self._sumOfLeftLeaves2(root.right)

