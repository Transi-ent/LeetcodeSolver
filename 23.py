# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Brutal Force, 超时了
    """
    def mergeKLists(self, lists: list) -> ListNode:

        dummyHead = ListNode(-1)
        cur = dummyHead
        while lists:
            p = 0
            while p<len(lists):
                if lists[p] is None:
                    lists.pop(p)
                else:
                    p += 1
            if not lists:
                break
            val = min( [node.val for node in lists] )
            cur.next = ListNode(val)
            cur = cur.next
            for i, node in enumerate(lists):
                if node.val == val:
                    lists[i] = node.next
                    break
        return dummyHead.next

class Solution2:
    """
    使用一个优先队列，将 K 个链表的头结点都放在优先队列中，
    ... 每次 pop 出一个最小值，然后加入pop出的节点的下一个节点，直至为 None。
    """

    def mergeKLists(self, lists: list) -> ListNode:
        import heapq
        if not lists:
            return None

        dummyHead = cur = ListNode(-1)
        pq = []
        for node in lists:
            while node:
                heapq.heappush(pq, node.val)
                node = node.next

        while len(pq)>0:
            val = heapq.heappop(pq)
            cur.next = ListNode(val)
            cur = cur.next

        return dummyHead.next



