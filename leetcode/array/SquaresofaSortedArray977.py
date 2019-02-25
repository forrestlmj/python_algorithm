# https://leetcode.com/problems/squares-of-a-sorted-array/
import math


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in A:
            result.append(int(math.pow(i,2)))
        result.sort()
        return result
        # p_index = 0
        # for p_index in range(len(A)):
        #     if A[p_index] >= 0:
        #         break
        # ne_list = [abs(i) for i in A[:p_index]]
        # ne_list.reverse()
        # po_list = A[p_index:]
        # ne_index = 0
        # po_index = 0
        # result = []
        # while ne_index < len(ne_list) and po_index < len(po_list):
        #     if ne_list[ne_index] >= po_list[po_index]:
        #         result.append(int(math.pow(po_list[po_index],2)))
        #         po_index +=1
        #     else:
        #         result.append(int(math.pow(ne_list[ne_index], 2)))
        #         ne_index += 1
        # for i in range(ne_index,len(ne_list)):
        #     result.append(int(math.pow(ne_list[ne_index], 2)))
        # for i in range(po_index, len(po_list)):
        #     result.append(int(math.pow(po_list[po_index], 2)))

        return result

def test_0():
    s = Solution()
    A = [-4,-1,0,3,10]
    assert s.sortedSquares(A) == [0,1,9,16,100]
    A = [-7,-3,2,3,11]
    assert s.sortedSquares(A) == [4,9,9,49,121]
    A = [-10,-3,-1]
    assert s.sortedSquares(A) == [1,9,100]

if __name__ == "__main__":
    test_0()