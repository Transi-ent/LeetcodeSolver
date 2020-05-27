# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    1，写一个函数，求一个节点在 BST 中的高度；
    2，遍历这个BST，求出该树中所有节点的最大值；
    """
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root: TreeNode) -> int:
            if root is None:
                return 0
            return max(height(root.left), height(root.right))+1
        if root is None:
            return 0
        maxNum = 0
        queue = [root]
        while queue:
            node = queue.pop()
            maxNum = max(maxNum, height(node.left)+height(node.right))

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return maxNum
