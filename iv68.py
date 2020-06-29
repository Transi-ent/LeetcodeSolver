# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    该解法没有利用 BST 的性质，「适用于所有的二叉树」
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def isParent(root: TreeNode, n: TreeNode)->bool:
            # 判断一个节点是否为另一个节点的子节点
            if root is None and n is not None:
                return False
            return root == n or isParent(root.left, n) or isParent(root.right, n)
        if isParent(p, q):
            return p
        if isParent(q, p):
            return q
        leftP = isParent(root.left, p)
        leftQ = isParent(root.left, q)
        rightP = isParent(root.right, p)
        rightQ = isParent(root.right, q)
        if leftP and rightQ:
            return root
        if leftQ and rightP:
            return root
        if leftP and leftQ:
            return self.lowestCommonAncestor(root.left, p, q)
        if rightP and rightQ:
            return self.lowestCommonAncestor(root.right, p, q)

class Solution2:
    """
    BST，对于节点node，左子树上的节点逗比他小，右子树上的节点都比她大
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>q.val:
            p, q = q, p
        if p.val < root.val < q.val:
            return root
        if p.val == root.val or q.val == root.val:
            return root
        if root.val<p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
