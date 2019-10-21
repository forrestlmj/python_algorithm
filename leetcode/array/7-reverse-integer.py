import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        re = 0
        neg = -1 if x<0 else 1
        x = abs(x)
        while(x!=0):
            a = x%10
            x = int(x/10)
            re = re*10+a
        if (abs(re) > (2 ** 31 - 1)):
            return 0
        return re*neg
def test0():
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(100) == 1
    assert s.reverse(10) == 1
    assert s.reverse(1534236469) == 0
if __name__ == "__main__":
    test0()