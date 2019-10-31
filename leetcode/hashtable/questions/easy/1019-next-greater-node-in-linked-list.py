# https://leetcode.com/problems/keyboard-row/
import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        l = list()
        while head:
            l.append(head.val)
            head = head.next
        l = l[::-1]
        re = list()
        stack = list()
        for i in l:
            while len(stack) > 0:
                if stack[-1] <= i:
                    stack.pop()
                else:
                    break

            if len(stack) == 0:
                stack.append(i)
                re.append(0)
            else:
                re.append(stack[-1])
                stack.append(i)

        re = re[::-1]
        return re
def turn_to_list(l):
    head = ListNode(l[0])
    d = head
    for i in l[1:]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    return d

def test():
    s = Solution()
    # c = s.deleteDuplicates(turn_to_list(l1))
    assert s.nextLargerNodes(turn_to_list([1,1])) == [0,0]
    assert s.nextLargerNodes(turn_to_list([2,1,1])) == [0,0,0]
    assert s.nextLargerNodes(turn_to_list([1,2,1,1])) == [2,0,0,0]

    assert s.nextLargerNodes(turn_to_list([2,1,5])) == [5,5,0]
    assert s.nextLargerNodes(turn_to_list([2,7,4,3,5])) == [7,0,5,5,0]
    assert s.nextLargerNodes(turn_to_list( [1,7,5,1,9,2,5,1])) == [7,9,9,9,0,5,0,0]
    # return c
    # r = []
    # while c:
    #     r.append(c.val)
    #     c = c.next
    # print(r)


if __name__ == "__main__":
    test()