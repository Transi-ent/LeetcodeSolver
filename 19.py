# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 1, Makes 2 pointers have a distance of n nodes.
        # 2, Move the right-pointer to the last upstream position

        right = head

        for i in range(n+1):
            if not right.next:
                return None
            right = right.next

        left = head
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 1, Makes 2 pointers have a distance of n nodes.
        # 2, Move the right-pointer to the last upstream position

        right = head
        removeFirst, removeSecond = False, False
        count = 0

        if n==1:
            if not right.next:
                return None
            while right.next:
                if not right.next.next:
                    right.next = None
                else:
                    right = right.next
            return head

        for i in range(n+1):
            # if not right.next:
            #     head = None
            #     return head
            if right.next:
                right = right.next
            else:
                if count == n:
                    removeSecond = True
                else:
                    removeFirst = True
            count += 1

        if removeFirst:
            return head.next

        left = head
        if removeSecond:
            left.right = left.next.next
            return head

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummyhead = ListNode(-1)
        dummyhead.next = head

        left = right = dummyhead

        while n:
            right = right.next
            n -= 1

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummyhead.next
