# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    每次都从原链表中取出一个节点，并将该节点插入到dummy节点之后:
    TODO:【链表问题法宝】———— Dummy Head
    """
    def reverseList(self, head: ListNode) -> ListNode:

        dummy = ListNode(-1)
        dummy.next = None
        while head:
            node = head
            head = head.next
            next = dummy.next
            dummy.next = node
            node.next = next

        return dummy.next
