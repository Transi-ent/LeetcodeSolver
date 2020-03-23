# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 使用 O(n)的时间复杂度和 O(n)的空间复杂度，判断列表内的元素是否回文
        lyst = []

        cur = head
        while cur:
            lyst.append(cur.val)
            cur = cur.next

        left, right = 0, len(lyst)-1
        while left<right:
            if lyst[left] != lyst[right]:
                return False
            left += 1
            right -= 1

        return True

    #def isPalindrome2(self, head: ListNode) -> bool:
