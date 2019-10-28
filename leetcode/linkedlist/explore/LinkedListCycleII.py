# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        使用双指针的方法解决，当快速指针遇到慢速指针时候，说明有循环
        """
        seen = set()
        if head is None:
            return None
        while(head.next is not None):
            if head in seen:
                return head
            else:
                seen.add(head)
            head = head.next
        return None
