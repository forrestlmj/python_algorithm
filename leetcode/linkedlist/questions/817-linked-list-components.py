# coding=utf-8
import sys


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        这道题的解法是把所给集合给链表涂色看链表　被分成了含有颜色的几组
        """
        dummy = ListNode(-1)
        dummy.next = head

        while head:
            if head.val in G:
                head.val = -1
            head = head.next
        c = dummy.next
        count = 0
        one_compent = False
        while c:
            if c.val == -1 and one_compent == False:
                one_compent = True
                count += 1
            if c.val != -1 and one_compent == True:
                one_compent = False
            c = c.next
        return count

def turn_to_list(l):
    head = ListNode(l[0])
    d = head
    for i in l[1:]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    return d

def test(l1,G):
    s = Solution()
    c = s.numComponents(turn_to_list(l1),G)
    # return c
    # r = []
    # while c:
    #     r.append(c.val)
    #     c = c.next
    print(c)

if __name__ == "__main__":
    test( [0,1,2,3],[0,1,3])
    test( [0,1,2,3,4],[0,3,1,4])
    # test( [0,1,2,3,4,5,6],[0,3,1,5])
    test( [0,1,2],[1,0])
    test([1,2,0,4,3],[3,4,0,2,1])
    #
    # test([1,2,3,4,5])
    # test([1,2,3,4,5,6])
