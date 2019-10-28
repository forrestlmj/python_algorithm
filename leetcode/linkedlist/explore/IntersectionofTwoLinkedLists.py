# coding=utf-8
#https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        pta,ptb,jumpToNext = headA,headB,False
        while pta and ptb:
            if pta == ptb:
                return pta
            pta,ptb = pta.next,ptb.next
            if not pta and not jumpToNext:
                pta = headB
                jumpToNext = True
            if not ptb:
                ptb = headA
        return None

# if __name__ == "__main__":
