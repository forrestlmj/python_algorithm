import sys


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        r = list()
        lenth = [0]*k
        dummy = ListNode(-1)
        dummy.next = root
        root_len = 0
        while root:
            root_len += 1
            root = root.next
        # print(root_len)
        base = int(root_len/k)
        # print(base)
        mod = root_len%k
        # print(mod)
        for i in range(len(lenth)):
            lenth[i] = base + (1 if i < mod else 0)
        # print(lenth)
        cur = dummy.next
        for i in lenth:
            if i >0:
                j = 0
                o = ListNode(-1)
                o.next = cur
                for j in range(0,i):
                    n = ListNode(cur.val)
                    o.next = n
                    if j == 0:
                        r.append(o.next)
                    o = n
                    if j == i-1:
                        o.next = None
                    cur = cur.next
            else:
                r.append(None)
        return r
def turn_to_list(l):
    head = ListNode(l[0])
    d = head
    for i in l[1:]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    return d

def test(l1,k):
    s = Solution()
    c = s.splitListToParts(turn_to_list(l1),k)
    # return c
    r = []
    # while c:
    #     r.append(c.val)
    #     c = c.next
    # print(r)

if __name__ == "__main__":
    test( [1, 2, 3], k = 5)
    test( [1, 2, 3], k = 2)
    test( [1, 2, 3], k = 1)

    test( [1, 2, 3], k = 3)

    test( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3)
    test( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 12)
    test( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 11)
    test( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 10)
    test( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 9)
    test( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 8)

    # test( [1],[0])
    # test( [9],[0])
    # test( [9],[1])
    # test( [9,9,9],[1])
    # test( [2,9,9,9],[1])
    # test( [1],[2,9,9,9])
    # test( [1],[2,9,9,9])

    # test( [1,1,2,3,3])
    # test( [11])
    # test( [11,12,12,12,12,13,13,13])

    #
    # test([1,2,3,4,5])
    # test([1,2,3,4,5,6])
