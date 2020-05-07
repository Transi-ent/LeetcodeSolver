# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 如果当前节点为 None，或者当前节点为叶子节点，将该节点返回
        if root is None or (root.left is None and root.right is None):
            return root
        # 将左右子树依次展开，即递归到底，自底向上的将树展开
        self.flatten(root.left)
        self.flatten(root.right)

        # 先将 右子树暂存下来
        tmp = root.right

        root.right = root.left
        root.left = None # 左子树一定要置 None，否则不能按题目要求的形成单链的拓扑结构；
        while root.right:
            root = root.right
        root.right = tmp
