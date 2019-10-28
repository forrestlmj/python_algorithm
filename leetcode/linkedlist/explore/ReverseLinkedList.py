class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        newHead = ListNode(-1)

        while (curr != None):
            NewNode = ListNode(curr.val)
            NewNode.next = newHead.next
            newHead.next = NewNode

            curr = curr.next

        return newHead.next