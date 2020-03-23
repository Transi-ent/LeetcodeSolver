# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 只需要打断一个连接，并且重建一个连接即可
        # 1，找到倒数第 K 个的上一个节点，断开连接；
        # 2，找到链表的末尾节点，指向头结点；
        def getLength(head: ListNode) -> int:
            n = 0
            if head is None:
                return 0
            while head:
                head = head.next
                n += 1
            return n

        if head is None or k==0:
            return head
        dummyhead = ListNode(-1)
        dummyhead.next = head

        left = right = dummyhead
        n = getLength(left.next)
        k = k % n
        while k:
            right = right.next
            k -= 1

        while right.next:
            left = left.next
            right = right.next

        newHead = left.next
        left.next = None
        right.next = head

        return newHead
