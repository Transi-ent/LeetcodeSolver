# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, arr: list):
        self.dummyhead = ListNode(-1)
        cur = self.dummyhead
        for e in arr:
            cur.next = ListNode(e)
            cur = cur.next

        #print("INIT: ",self.dummyhead.next.val)

    def head(self):
        return self.dummyhead.next

def printLinkedList(ll: ListNode):
    while ll:
        print(ll.val, end=' ')
        if ll.next:
            print('->', end=' ')
        ll = ll.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummyhead = ListNode(-1)
        cur = dummyhead
        flag = 0
        while l1 and l2:
            sumVal = l1.val + l2.val + flag
            l1 = l1.next
            l2 = l2.next
            if sumVal>9:
                flag, sumVal = divmod(sumVal, 10)
            else:
                flag = 0

            cur.next = ListNode(sumVal)
            cur = cur.next

        while flag or l1 or l2:# 若还可以继续进位
            if l1:
                sumVal = l1.val + flag
                l1 = l1.next
            elif l2:
                sumVal = l2.val + flag
                l2 = l2.next
            elif flag==1:
                cur.next = ListNode(1)
                break

            if sumVal>9:
                flag, sumVal = divmod(sumVal, 10)
            else:
                flag = 0

            cur.next = ListNode(sumVal)
            cur = cur.next

        return dummyhead.next

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyhead = ListNode(-1)
        cur = dummyhead

        flag = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + flag
            if val>9:
                flag, val = divmod(val, 10)
            else:
                flag = 0
            cur.next = ListNode(val)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if flag:
            cur.next = ListNode(flag)

        return dummyhead.next



ll1 = LinkedList([2,4,3]).head()
ll2 = LinkedList([5,6,4]).head()
ret = Solution().addTwoNumbers(ll1, ll2)
printLinkedList(ret)

