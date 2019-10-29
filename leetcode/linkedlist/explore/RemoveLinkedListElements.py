# encoding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        如果能快指针匹配到，慢指针不动，否则都动
        """
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy.next
        slow = dummy

        while fast:
            if fast.val == val:
                slow.next = fast.next
                slowShouldMoved = False
            else:
                slowShouldMoved = True
            fast = fast.next
            if slowShouldMoved:
                slow = slow.next
        return dummy.next