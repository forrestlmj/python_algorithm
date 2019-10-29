# encoding=utf-8
class ListNode(object):
    def __init__(self,val):
        self.next = None
        self.val = val
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        注意一些情况下链表涉及到删减时要从链表的头的前一个开始算起
        """
        length = 0

        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        slow = dummy
        while length <= n:
            fast = fast.next
            length += 1
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next