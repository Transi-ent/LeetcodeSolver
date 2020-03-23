# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        1, move the pointer to the given position.
        2, reverse the LinkedList of the given segment.
        :param head:
        :param m:
        :param n:
        :return:
        """
        t = n - m
        if m == 1:

            cur = head
            while t>0:
                node1 = cur
                node2 = cur.next
                node3 = cur.next.next

                node2.next = head
                head = node2
                node1.next = node3
                t -= 1
        else:
            begin = head
            for i in range(m-2):
                begin = begin.next

            cur = begin.next

            while t>0:

                node1 = cur
                node2 = cur.next
                node3 = cur.next.next

                # node2.next = node1
                # node1.next = node3
                front = begin.next
                begin.next = node2
                node2.next = front
                node1.next = node3

                t -= 1

        return head
