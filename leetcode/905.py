class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key = lambda k:k%2)
        return A

def test():
    A = [3, 1, 2, 4]
    s = Solution()
    print(s.sortArrayByParity(A))
test()