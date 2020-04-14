# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, l: list):
        self.dummyhead = ListNode(-1)
        cur = self.dummyhead
        for em in l:
            cur.next = ListNode(em)
            cur = cur.next

    def head(self):
        return self.dummyhead.next

def printLinkedList(l: ListNode):
    while l:
        print(l.val, end=' ')
        if l.next:
            print('->', end='')
        l = l.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = 0, 0

        while l1 or l2:
            if l1:
                n1 = 10*n1 + l1.val
                l1 = l1.next
            if l2:
                n2 = 10*n2 + l2.val
                l2 = l2.next

        res = n1 + n2
        next = None
        while res>9:
            res, rem = divmod(res, 10)
            cur = ListNode(rem)
            cur.next = next
            next = cur


        head = ListNode(res)
        head.next = next
        return head




ll1 = LinkedList([7,2,4,3]).head()
ll2 = LinkedList([5,6,4]).head()
ret = Solution().addTwoNumbers(ll1, ll2)
printLinkedList(ret)
