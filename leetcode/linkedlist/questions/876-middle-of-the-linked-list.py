class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        dummy = ListNode(-1)
        dummy.next = head
        while head:
            length += 1
            head = head.next
        mid =  int(length/2)
        for i in range(0,mid):
            dummy = dummy.next
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
    c = s.middleNode(turn_to_list(l1))
    # return c
    r = []
    while c:
        r.append(c.val)
        c = c.next
    print(r)

if __name__ == "__main__":
    test([1])
    test([1,2])

    test([1,2,3,4,5])
    test([1,2,3,4,5,6])
