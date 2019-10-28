# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        使用双指针的方法解决，当快速指针遇到慢速指针时候，说明有循环
        """
        if (head == None or head.next == None):
            return False
        slow = head
        fast = head.next
        while(slow != fast):
            if (fast == None or fast.next == None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True
