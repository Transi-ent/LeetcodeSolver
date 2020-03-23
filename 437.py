# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        TODO: 递归的搜索当前节点被包含在路径中时的路径，和当前节点不被包含在路径中时的路径
        :param root:
        :param sum:
        :return:
        """
        if root is None:
            return 0

        res = 0
        # 包含当前节点在内的，所有 PathSum 总数
        res = self.findPath(root, sum, res)
        # 不包含该根节点在内的所有 PathSum 总数
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res

    def findPath(self, root: TreeNode, sum: int, res: int) -> int:

        if root is None:
            return 0

        if root.val == sum:
            res += 1
            return res
        else:
            tmp = res
            res += self.findPath(root.left, sum - root.val, tmp)
            res += self.findPath(root.right, sum - root.val, tmp)
            return res

