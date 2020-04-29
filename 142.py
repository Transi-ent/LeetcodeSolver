# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        fast = slow = cur = head
        while fast.next:
            if fast.next.next is None:
                return None

            if fast.next.next == slow.next:
                break
            else:
                fast = fast.next.next
                slow = slow.next

        if fast.next is None:
            return None

        nodeSet = set()
        while not slow.next in nodeSet:
            nodeSet.add(slow.next)
            slow = slow.next

        i = 0
        while not cur in nodeSet:
            cur = cur.next
            i += 1
        return cur
