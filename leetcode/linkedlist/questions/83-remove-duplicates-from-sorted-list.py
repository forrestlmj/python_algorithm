import sys


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cu = head
        while head.next:
            if cu.val == head.next.val:
                cu.next = head.next.next
            else:
                cu = cu.next
                head = head.next
        return dummy.next
def turn_to_list(l):
    head = ListNode(l[0])
    d = head
    for i in l[1:]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    return d

def test(l1):
    s = Solution()
    c = s.deleteDuplicates(turn_to_list(l1))
    # return c
    r = []
    while c:
        r.append(c.val)
        c = c.next
    print(r)

if __name__ == "__main__":
    test( [1,1,2])
    test( [1,1,2,3,3])
    test( [11])
    test( [11,12,12,12,12,13,13,13])

    #
    # test([1,2,3,4,5])
    # test([1,2,3,4,5,6])
