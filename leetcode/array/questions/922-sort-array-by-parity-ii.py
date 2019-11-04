import sys


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l_odd = list() # 奇数
        l_even = list() # 偶数
        for i in range(len(A)):
            if i%2 == A[i]%2:
                pass
            else:
                if A[i]%2 == 0:
                    l_even.append(A[i])
                else:
                    l_odd.append(A[i])
                A[i] = -1*sys.maxsize
        for i in range(len(A)):
            if A[i]<0:
                if i%2 == 0:
                    A[i] = l_even.pop()
                else:
                    A[i] = l_odd.pop()
        return A
s = Solution()
print(s.sortArrayByParityII( [4,2,5,7]))
print(s.sortArrayByParityII( [0,1]))