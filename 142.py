# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    双指针，使用一个额外的集合来记录所走过的节点。
    时间复杂度 O(N),空间复杂度 O(b), b 为环长度
    """
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

class Solution2:
    """
    双指针，结合数学法
    时间复杂度 O(N),空间复杂度 O(1)
    假设 fast、slow 相遇时，slow 走了s，则fast走了 2s，fast 比 slow 多走了 n 圈
    若从头结点到环入口点有 a 个节点，环上有 b 个节点，则相遇时 fast 走了 s+nb，
    所以，s=nb，然后 slow 沿路继续走 a 步后路程变为 a + nb，即刚好回到环入口点。
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while True:
            if fast is None or fast.next is None:
                return None
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
