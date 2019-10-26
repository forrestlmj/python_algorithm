# https://leetcode.com/problems/count-primes/
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <2:
            return 0
        composite_set = set()
        for i in range(2,n):
            if i in composite_set:
                pass
            else:
                for j in range(i,n):
                    if i * j > n:
                        break
                    else:
                        composite_set.add(i*j)
        if n in composite_set:
            return n-1-len(composite_set)
        else:
            return n-2-len(composite_set)
def test():
    s = Solution()
    # s.countPrimes(10)
    assert s.countPrimes(10) == 4
    # assert s.countPrimes(11) == 5
    # assert s.countPrimes(12) == 5
    assert s.countPrimes(0) == 0
    assert s.countPrimes(1) == 0
    assert s.countPrimes(2) == 0
    assert s.countPrimes(3) == 1
    assert s.countPrimes(4) == 2
    assert s.countPrimes(5) == 2
    assert s.countPrimes(23) == 8
if __name__ == "__main__":
    test()