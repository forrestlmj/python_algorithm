class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N ==1 or N == 0:return N
        else:
            return self.fib(N-1)+self.fib(N-2)
s = Solution()
print(s.fib(0))
print(s.fib(1))
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
print(s.fib(5))