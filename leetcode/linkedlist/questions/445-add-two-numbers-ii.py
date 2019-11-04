import sys


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse(self,head):
        if not head.next:
            return head
        fast = head.next
        slow = ListNode(head.val)
        while fast:
            a = ListNode(fast.val)
            a.next = slow
            slow = a
            fast = fast.next
        return slow
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r1 = self.reverse(l1)
        r2 = self.reverse(l2)
        re = None
        carry = 0
        while r1 or r2 or carry > 0:
            r1v,r2v = r1.val if r1 else 0,r2.val if r2 else 0
            new_re = ListNode((r1v+r2v+carry)%10)
            new_re.next = re
            re = new_re
            carry = int((r1v+r2v+carry)/10)
            r1,r2 = r1.next if r1 else None,r2.next if r2 else None
        return re
def turn_to_list(l):
    head = ListNode(l[0])
    d = head
    for i in l[1:]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    return d

def test(l1,l2):
    s = Solution()
    c = s.addTwoNumbers(turn_to_list(l1),turn_to_list(l2))
    # return c
    r = []
    while c:
        r.append(c.val)
        c = c.next
    print(r)

if __name__ == "__main__":
    test( [7,2,4,3],[5,6,4])
    test( [5,6,4],[7,2,4,3])
    test( [1],[0])
    test( [9],[0])
    test( [9],[1])
    test( [9,9,9],[1])
    test( [2,9,9,9],[1])
    test( [1],[2,9,9,9])
    test( [1],[2,9,9,9])

    # test( [1,1,2,3,3])
    # test( [11])
    # test( [11,12,12,12,12,13,13,13])

    #
    # test([1,2,3,4,5])
    # test([1,2,3,4,5,6])
