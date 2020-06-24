# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    从一个头结点开始，将遍历过的节点放入集合中，
    再从另一个头结点开始遍历，已经遍历过的节点即为第一个公共头结点
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        nodes = set()
        while headA:
            nodes.add(headA)
            headA = headA.next

        while headB:
            if headB in nodes:
                return headB
            headB = headB.next
