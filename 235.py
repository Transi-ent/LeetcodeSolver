class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root:'TreeNode',p:'TreeNode',q:'TreeNode')->'TreeNode':
        """
        节点 p 和 q 的最低公共祖先必然是在 p、q 的取值区间内，或者 p、q 互为父子节点
        :param root:
        :param p:
        :param q:
        :return:
        """
        if root is None:
            return root

        if p is None or q is None:
            return None

        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
