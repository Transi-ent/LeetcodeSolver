class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        vals = set()
        if head is None:
            return head

        vals.add(head.val)
        head1 = head
        while head1.next:# 在 head.next 不为 None的情况下
            if head1.next.val in vals:
                head1.next = head1.next.next
            else:
                head1 = head1.next
                vals.add(head1.val)
        return head

