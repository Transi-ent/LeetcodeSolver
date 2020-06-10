
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """
    递归，利用原链表各节点之间的拓扑关系递归，在递归的过程中原样复制
    通过指针（next指针和random指针，在节点之间建立连接）
    我们的目的是拷贝原链表的每一个节点，并返回复制后链表的头节点
    """
    def __init__(self):
        self.visited = {} # 字典中存放的是 oldNode: newNode 节点对，以免链表中存在环

    def copyRandomList(self, head: Node) -> Node:

        if head is None:# 递归到底时
            return head

        if head in self.visited:
            return self.visited[head]

        # 当该节点不为空，且并未遍历过时
        node = Node(head.val, None, None)
        self.visited[head] = node# 放入到遍历过的哈希表内

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

