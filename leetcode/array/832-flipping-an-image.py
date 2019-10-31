import sys


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # B = list()
        for row in A:
            row.reverse()
        for line in A:
            for i in range(len(line)):
                line[i] = (line[i]+1)%2
        return A


def test0():
    s = Solution()
    assert s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]
    assert s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

if __name__ == "__main__":
    test0()