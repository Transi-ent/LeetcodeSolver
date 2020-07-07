# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 从根节点到叶子节点，路径上所有节点取值之和为目标值
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == sum

        return self.hasPathSum(root.left, sum-root.val) or \
               self.hasPathSum(root.right, sum-root.val)

    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:

        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == sum

        return self.hasPathSum2(root.left, sum-root.val) or \
            self.hasPathSum2(root.right, sum-root.val)

class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left == None and root.right == None:
            if root.val==sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum-root.val) or \
               self.hasPathSum(root.right, sum-root.val)
