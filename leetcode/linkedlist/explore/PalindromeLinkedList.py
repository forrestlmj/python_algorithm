# encoding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    stack = list()
    def reverse(self,head):
        last = ListNode(head.val)
        # p = ListNode(-1)
        p = head.next
        while(p):
            newNode= ListNode(p.val)
            newNode.next = last
            last = newNode
            p = p.next
        return last
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        len = 0
        dummy_head = ListNode(-1)
        dummy_head.next = head
        tail = self.reverse(head)
        while tail and head:
            if head.val == tail.val:
                pass
            else:
                return False
            head = head.next
            tail = tail.next

        return True
def test(l):
    # l = [1, 2, 3, 4, 5, 6, 7, 8]
    head = ListNode(l[0])
    d = head
    for i in l[1:]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    s = Solution()
    c = s.isPalindrome(d)
    return c
    # r = []
    # while c:
    #     r.append(c.val)
    #     c = c.next
    # print(r)

if __name__ == "__main__":
   assert test([]) == False

   assert test([1]) == True
   assert test([1,2]) == False
   assert test([1,2,2,1]) == True
   assert test([1,2,3,2,1]) == True
   assert test([1,2,3,1,1,3,2,1]) == True
   # test([1,2,3])