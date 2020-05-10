# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    当两个节点互为父子节点时，最近的公共节点就是父节点本身；
    否则，必为一个节点在左子树，一个节点在右子树；
    超时
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root.val == p.val and self.find(root, q):
            return root
        if root.val == q.val and self.find(root, p):
            return root
        if (self.find(root.left, p) and self.find(root.right, q)) or\
            ( self.find(root.left, q) and self.find(root.right, p) ):
            return root
        if self.find(root.left, p) and self.find(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.find(root.right, p) and self.find(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)

    def find(self, root: TreeNode, target: TreeNode )->bool:
        """
        在以 root 为根节点子树上寻找节点 target
        :param root:
        :param target:
        :return:
        """
        if root is None:
            return False
        if root.val == target.val:
            return True
        return self.find(root.left, target) or self.find(root.right, target)

class Solution2:
    """
    当两个节点互为父子节点时，最近的公共节点就是父节点本身；
    否则，必为一个节点在左子树，一个节点在右子树；
    超时
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 递归到底的情况，如果节点 p, q 互为父子节点，找到父节点就直接返回，不会继续递归
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root
