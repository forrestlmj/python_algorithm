class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val,node.next = node.next.val,node.next.next

def turn_to_list(l):
    head = ListNode(l[0])
    d = head
    for i in l[1:]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    return d

def test(l1,node):
    s = Solution()
    c = s.deleteNode(turn_to_list(l1),node)
    # return c
    r = []
    while c:
        r.append(c.val)
        c = c.next
    print(r)

if __name__ == "__main__":
    test( [4,5,1,9],5)
    test(head = [4,5,1,9], node = 1)
    #
    # test([1,2,3,4,5])
    # test([1,2,3,4,5,6])
