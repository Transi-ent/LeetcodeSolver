# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
        Get the result of the level-order,
        ...and extract the last element of each level
        :param root:
        :return:
        """
        if root is None:
            return []

        queue, res = [root], []
        while queue:
            layer = queue

            queue = []
            layerRes = []

            for node in layer:
                layerRes.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(layerRes)

        res = [em[-1] for em in res]

        return res
