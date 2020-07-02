# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    之前已经做过BST，现在是二叉树
    对于一个二叉树，2个指定节点的最近公共祖先一定满足：
    1，其中一个是另一个的祖先，本身也可以是自己的祖先；
    2，存在一个节点W，这 2 个节点一个在其左子树，一个在其右子树上
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def isParent(root: TreeNode, son: TreeNode)->bool: # 判断两个节点是否存在父子关系
            if root is None and son is not None:
                return False
            return root == son or isParent(root.left, son) or isParent(root.right, son)

        if isParent(p, q):
            return p
        if isParent(q, p):
            return q
        if (isParent(root.left, p) and isParent(root.right, q)) or \
                (isParent(root.left, q) and isParent(root.right, p)):
            return root
        if isParent(root.left, p) and isParent(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if isParent(root.right, p) and isParent(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)

