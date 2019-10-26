# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        rep = set()
        for i in A:
            if i not in rep:
                rep.add(i)
            else:
                return i

def test():
    s = Solution()
    assert s.repeatedNTimes([1,2,3,3]) ==3
    assert s.repeatedNTimes( [2,1,2,5,3,2]) == 2
    assert s.repeatedNTimes([5,1,5,2,5,3,5,4]) == 5
    print("ok")

if __name__ == "__main__":
    test()
