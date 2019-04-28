import sys
class Solution(object):
    def is_crosed(self,l1,l2):
        if (l1[0]-l2[0]) * (l1[1]-l2[1]) < 0:
            return True
        elif l1[0] == l2[0] or l1[1] == l2[1]:
            return True
        else:
            return False
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        l = []
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    l.append((i,j))
        l_dict = {}

        for i in range(len(l)):
            t = list()
            for j in range(len(l)):
                if not self.is_crosed(l[i],l[j]):
                    # print(l[i], l[j])
                    t.append(l[j])
            l_dict[l[i]] = t
        min_line =sys.maxsize
        index = 0
        for i in l_dict:
            tmp = l_dict[i]
            tmp_l = len(l_dict[i])
            min_line = len(l_dict[i]) if len(l_dict[i]) < min_line else min_line
        print(min_line)
        return min_line

def test_0():
    s = Solution()
    A = [1, 4, 2]
    B = [1, 2, 4]
    s.maxUncrossedLines(A,B)

    # assert s.maxUncrossedLines(A,B) == 2
    A = [2,5,1,2,5]
    B = [10,5,2,1,5,2]
    s.maxUncrossedLines(A,B)

    # assert s.maxUncrossedLines(A,B) == 3
    A = [1,3,7,1,7,5]
    B = [1,9,2,5,1]
    s.maxUncrossedLines(A,B)
    # assert s.maxUncrossedLines(A,B) == 2

if __name__ == "__main__":
    test_0()