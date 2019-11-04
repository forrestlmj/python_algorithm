# https://leetcode.com/problems/count-primes/
import math


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        d = dict()
        for i in candies:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        return min(len(candies)/2,len(d.keys()))


def test():
    s = Solution()
    assert s.distributeCandies(candies = [1,1,2,2,3,3]) == 3

    assert s.distributeCandies(candies = [1,1,2,3]) == 2


if __name__ == "__main__":
    test()