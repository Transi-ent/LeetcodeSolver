# Definition for singly-linked list.
#TODO: 「 未解决 」
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Take advantage of dummyHead, insert all the nodes of l2 into l1
        dummyhead = ListNode(-float('inf'))
        dummyhead.next = l1
        cur1, cur2 = dummyhead, l2

        while cur2:
            if cur1.next:
                if cur1.val < cur2.val <= cur1.next.val:
                    print("cur1:",cur1.val, "   cur2:", cur2.val)
                    # Insertion Operation
                    nex = cur1.next
                    cur2Copy = cur2
                    cur1.next = cur2Copy
                    cur2Copy.next = nex

                    # Move pointer
                    cur2 = cur2.next
                    cur1 = cur1.next

                    print("cur1:", cur1.val, "   cur2:", cur2.val)

                else:
                    print("cur1:", cur1.val, "   cur2:", cur2.val)
                    cur1 = cur1.next
                    print("cur1:", cur1.val, "   cur2:", cur2.val)
            else:
                # LinkedList l2 can only insert into the end of linkedList l1
                print("cur1:", cur1.val, "   cur2:", cur2.val)
                cur2Copy = cur2

                cur1.next = cur2Copy
                cur2Copy.next = None
                cur1 = cur1.next
                cur2 = cur2.next
                print("cur1:", cur1.val, "   cur2:", cur2.val)

        return dummyhead.next
