# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # As a sorted LinkedList, just check it continuously
        dummyhead = ListNode(0)
        dummyhead.next = head
        s = set()

        cur = dummyhead
        while cur.next:
            if cur.next.val in s :
                cur.next = cur.next.next
                continue

            if cur.next.next and cur.next.val==cur.next.next.val:
                if not cur.next.val in s:
                    s.add(cur.next.val)

                cur.next = cur.next.next.next
                continue

            cur = cur.next

        return dummyhead.next


