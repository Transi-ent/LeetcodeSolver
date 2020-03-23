# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        n = 0
        dummyhead = ListNode(0)
        dummyhead.next = head
        cur = dummyhead
        while cur.next and cur.next.next:
            if n % 2 == 0:
                node1 = cur.next
                node2 = cur.next.next
                node3 = node2.next

                cur.next = node2
                node2.next = node1
                node1.next = node3

            cur = cur.next
            n += 1

        return dummyhead.next

