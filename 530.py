# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    #     return self.__getMinimumDifference(root, float('inf'))
    #
    # def __getMinimumDifference(self, root, minAbs):
    #
    #     if root is None:
    #         return minAbs
    #
    #     if root.left is None and root.right is None:
    #         return minAbs
    #
    #     if root.left is not None:
    #         minAbs_left = min(minAbs, abs(root.val - root.left.val))
    #         left = self.__getMinimumDifference(root.left, minAbs_left)
    #
    #     if root.right is not None:
    #         minAbs_right = min(minAbs, abs(root.val - root.right.val))
    #         right = self.__getMinimumDifference(root.right, minAbs_right)
    #
    #     return min(left, right, )

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
    # Get the in-order sequence, it's a sorted list
    lyst = list()
    lyst = self.inOrder(root, lyst)

    def inOrder(self, root, lyst):

        if root.left is not None:
            self.inOrder(root.left)

