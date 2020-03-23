"""
Reverse the linkedList
"""

class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode):

    prev = None


    while head:

        next = head.next # if head!=null, thus head.next exists

        # 三个指针的位置都已经就绪，可以翻转了
        head.next = prev

        prev = head

        head = next

    return prev


def createLinkedList(arr: list, n):

    if not n:
        return None

    cur = ListNode(arr[0])

    for i in range(1, n):

        cur.next = ListNode(arr[i])

        cur = cur.next

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        cur = head
        while cur and cur.next:
            node1 = cur
            node2 = cur.next
            node3 = cur.next.next

            node2.next = head
            head = node2
            node1.next = node3

        return head





















