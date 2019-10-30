# encoding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_l1 = ListNode(-1)
        dummy_l1.next = l1
        dummy_l2 = ListNode(-2)
        dummy_l2.next = l2
        re = ListNode(-1)
        l1_is_bigger =  False
        while l1 and l2:
            if l1.val >= l2.val:
                l1_is_bigger = True
            else:
                l1_is_bigger = False
            if l1_is_bigger:
                re.next = l2
                re =re.next
                re.next = l1
            else:
                re.next = l1
                re =re.next
                re.next = l2
            l1 = l1.next
            l2 = l2.next


        if not l1:
            re.next = l2
        if not l2:
            re.next = l1
        return dummy_l1.next
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
    c = s.mergeTwoLists(turn_to_list(l1),turn_to_list(l2))
    # return c
    r = []
    while c:
        r.append(c.val)
        c = c.next
    print(r)

if __name__ == "__main__":
    test([1,2,4],[1,3,4])

   # assert test([1]) == True
   # assert test([1,2]) == False
   # assert test([1,2,2,1]) == True
   # assert test([1,2,3,2,1]) == True
   # assert test([1,2,3,1,1,3,2,1]) == True
   # test([1,2,3])