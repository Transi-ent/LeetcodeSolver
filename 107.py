# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:

        if root is None:
            return []

        queue, res, level = [root], [], 0
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

            if level % 2 == 1:
                layerRes[:] = layerRes[::-1]
            res.append(layerRes)
            level += 1

        return res
