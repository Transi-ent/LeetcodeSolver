class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        tail = head
        for i in range(k):
            tail = tail.next

        cur = head
        while tail:
            cur = cur.next
            tail = tail.next

        return cur.val
