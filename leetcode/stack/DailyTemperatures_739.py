# https://leetcode.com/problems/daily-temperatures/
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        o = [0 for i in range(len(T))]
        stack = list()
        for i in range(len(T)):
            for j in range(i+1,len(T)):
                if T[i] < T[j]:
                    o[i] = j-i
                    break
        return o

def test_0():
    s = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    assert s.dailyTemperatures(T) == [1, 1, 4, 2, 1, 1, 0, 0]
if __name__ == "__main__":
    test_0()