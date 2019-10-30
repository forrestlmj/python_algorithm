# encoding=utf-8
# Definition for singly-linked list.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.child = child
        self.next = next
        self.prev = prev
        self.val = val
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        dummy_node = Node(None,None,None,1)
        dummy_node.next = head
        cur = head
        while(cur):
            if cur.child is None:
                pass
            else:
                stack.append(cur.next)
                cur.next = cur.child
                cur.child = None
            if cur.next is not None:
                cur = cur.next
            else:
                break

        while len(stack) > 0:
            t = stack.pop()
            t.prev = cur
            cur.next = t
            while cur.next:
                cur = cur.next
        return dummy_node.next
def test(l):
    # l = [1, 2, 3, 4, 5, 6, 7, 8]
    head = Node(l[0])
    d = head
    for i in l[1:]:
        tmp = Node(i)
        head.next = tmp
        head = head.next
    s = Solution()
    c = s.oddEvenList(d)
    r = []
    while c:
        r.append(c.val)
        c = c.next
    print(r)
# def test1():
#     l = [1, 2, 3, 4, 5, 6, 7]
#     head = ListNode(l[0])
#     d = head
#     for i in l[1:]:
#         tmp = ListNode(i)
#         head.next = tmp
#         head = head.next
#     s = Solution()
#     c = s.oddEvenList(d)
#     while c.next:
#         print(c.val)
#         c = c.next
if __name__ == "__main__":
   test([1])
   test([1,2])
   test([1,2,3])
   test([1,2,3,4])
   test([1,2,3,4,5,6,7,8])
   test([1,2,3])