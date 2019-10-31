import sys


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != l[i]:
                count += 1
        return count

def test0():
    s = Solution()
    assert s.heightChecker([1,1,4,2,1,3]) == 3
    assert s.heightChecker([2,1,4,1,1,3]) == 5

if __name__ == "__main__":
    test0()