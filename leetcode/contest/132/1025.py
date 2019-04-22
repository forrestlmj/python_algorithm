import math


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N%2 ==0
    #     if N == 1:
    #         return False
    #     turn_time =0
    #     while(True):
    #         re = self.get_divisor(N)
    #         N = N-re
    #         if(N<=1):
    #             break
    #         else:
    #             turn_time+=1
    #     return turn_time%2 == 0
    #
    # def get_divisor(self,x):
    #     i = 1
    #     max_divisor = i
    #     while(i<x):
    #         if x%i == 0:
    #             if max_divisor < i:
    #                 max_divisor = max(i,x%i)
    #
    #         i+=1
    #     return max_divisor




def test_0():
    s = Solution()
    # print(s.get_divisor(100))
    # print(s.get_divisor(2))
    # print(s.get_divisor(3))
    # print(s.get_divisor(0))
    # print(s.get_divisor(1))
    # print(s.get_divisor(27))
    # print(s.get_divisor(99))
    print(s.divisorGame(2))
    print(s.divisorGame(3))
    # print(s.divisorGame(4))
    print(s.divisorGame(4))
    print(s.divisorGame(27))
    print(s.divisorGame(99))
    print(s.divisorGame(100))

if __name__ == "__main__":
    test_0()