# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        if A is None or B is None:
            return False

        return self.isSame(A, B) or \
               self.isSubStructure(A.left, B) or \
               self.isSubStructure(A.right, B)

    def isSame(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None and B is None:
            return True

        if A is None and B is not None:
            return False

        if A is not None and B is None:
            return True

        return A.val==B.val and self.isSame(A.left, B.left) and \
               self.isSame(A.right, B.right)
