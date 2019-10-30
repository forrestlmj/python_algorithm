# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jin = 0
        dummy_re = ListNode(-1)
        re = ListNode(-1)
        dummy_re.next = re
        while l1 or l2 or jin > 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = jin+a+b
            re.val = int(sum%10)
            jin = int(sum/10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2 and jin == 0:
                break
            new_re = ListNode(-1)
            re.next = new_re

            re = re.next
        return dummy_re.next
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
    test([2,4,3],[5,6,4])
    test([2,4,3,1],[5,6,4])
    test([0],[5,6,4])
    test([0],[0])
    test([9,9,9],[1,1,1,1])
    test([9],[1])

   # assert test([1]) == True
   # assert test([1,2]) == False
   # assert test([1,2,2,1]) == True
   # assert test([1,2,3,2,1]) == True
   # assert test([1,2,3,1,1,3,2,1]) == True
   # test([1,2,3])