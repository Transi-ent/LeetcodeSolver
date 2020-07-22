# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list:
        if(n==0):
            return []
        def build_Trees(left,right):
            all_trees=[]
            if(left>right):
                return [None]
            for i in range(left,right+1):
                left_trees=build_Trees(left,i-1)
                right_trees=build_Trees(i+1,right)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree=TreeNode(i)
                        cur_tree.left=l
                        cur_tree.right=r
                        all_trees.append(cur_tree)
            return all_trees
        res=build_Trees(1,n)
        return res

class Solution2:
    def generateTrees(self, n: int) -> list:
        if n==0:
            return []
        def buildTree(left: int, right: int):
            allTree = []
            if left>right:
                return [None]

            # 以每种情况为根节点进行递归
            for i in range(left, right+1):
                leftTree = buildTree(left, i-1)
                rightTree = buildTree(i+1, right)
                for l in leftTree:
                    for r in rightTree:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        allTree.append(cur)
            return allTree
        return buildTree(1, n)

