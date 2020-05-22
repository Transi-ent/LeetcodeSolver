# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, lyst: list):
        self.dummyHead = ListNode(-1)
        tail = self.dummyHead
        for val in lyst:
            tail.next = ListNode(val)
            tail = tail.next

    def head(self):
        return self.dummyHead.next

def printList(tail: ListNode):
    while tail:
        print(tail.val, ' ->', end=' ')
        tail = tail.next


class Solution:
    """
    1，使用自底向上的归并，因为不能递归；
    有 3 个关键操作 ：
        1）merge: 对两个链表进行归并；
        2）cut(head, step): 给一个链表，返回后半部分
        3）dummyHead;
    """
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        tail = head
        while tail:
            length += 1
            tail = tail.next

        dummyHead = ListNode(-1)
        dummyHead.next = head

        for i in range(0, length):
            if 2**i>length:
                break
            step = 2**i # 每次循环 step 都会扩大一倍
            tail = dummyHead # tail 用于记录排过序的链表的最后一个节点
            currentNode = dummyHead.next # currentNode 用于记录尚未拍过序的链表的头结点
            while currentNode:
                left = currentNode

                # 减掉 2 个链表片段，用于归并排序
                right = self.cut(left, step)
                currentNode = self.cut(right, step)

                tail.next = self.merge(left, right)
                while tail.next:
                    #print(tail.next.val, '->', end=' ')
                    tail = tail.next

        return dummyHead.next

    def merge(self, node1: ListNode, node2: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        tail = dummyHead
        while node1 and node2:

            if node1.val<node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next

            tail = tail.next

        tail.next = node1 if node1 else node2
        return dummyHead.next

    def cut(self, head: ListNode, n: int) -> ListNode:
        tail = head
        while tail and n:
            tail = tail.next
            n -= 1

        if tail is None:
            return None
        ret = tail.next
        tail.next = None
        return ret

    # def cut(self, head: ListNode, step: int):
    #     """从链表中截取步长为step的段"""
    #     p = head
    #     while p and step:
    #         p = p.next
    #         step -= 1
    #     if p is None:
    #         return None
    #     next = p.next  # 返回截断的后半部分
    #     p.next = None  # 截断
    #     return next

def merge(node1: ListNode, node2: ListNode) -> ListNode:
    dummyHead = ListNode(-1)
    tail = dummyHead
    while node1 and node2:

        if node1.val<node2.val:
            tail.next = node1
            node1 = node1.next
        else:
            tail.next = node2
            node2 = node2.next

        tail = tail.next

    tail.next = node1 if node1 else node2
    return dummyHead.next
l1 = LinkedList([4,2,1,3])
l2 = LinkedList([2,2,3,3])
ret = merge(l1.head(), l2.head())
l1 = Solution().sortList(l1.head())
printList(l1)
