# encoding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head为空
        if not head:
            return
        # 奇数指针指向head
        dummy_odd = ListNode(-1)
        dummy_odd.next = head
        # 如果就一个head，返回
        if not head.next:
            return dummy_odd.next
        dummy_even = ListNode(-1)
        dummy_even.next = head.next
        odd = head
        even = head.next
        oddTurn = True
        while odd and even:
            if oddTurn:
                odd.next = even.next
                if odd.next is None:
                    break
                odd = odd.next
                oddTurn = False
            else:
                even.next = odd.next
                even = even.next
                oddTurn =True

        odd.next = dummy_even.next
        return dummy_odd.next
def test(l):
    # l = [1, 2, 3, 4, 5, 6, 7, 8]
    head = ListNode(l[0])
    d = head
    for i in l[1:]:
        tmp = ListNode(i)
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