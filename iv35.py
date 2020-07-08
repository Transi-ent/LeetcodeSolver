# Definition for a Node.
import copy

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """
    使用DFS，并记录遍历过的节点，否则的话递归栈会溢出（因为可能存在环）
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        def copyList(head: Node) ->Node:
            if head is None:
                return head
            if head in visited:
                return visited[head]
            node = Node(head.val, None, None)
            visited[head] = node
            node.next = copyList(head.next)
            node.random = copyList(head.random)

            return node
        visited = {}
        return copyList(head)

class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)
