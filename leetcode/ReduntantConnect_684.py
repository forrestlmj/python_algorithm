# https://leetcode.com/problems/redundant-connection/
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        The size of the input 2D-array will be between 3 and 1000.
        Every integer represented in the 2D-array will be between 1 and N,
        where N is the size of the input array.
        也就是说N条边的树增加一条边生成图,现在需要去掉这个边
        也就是每增加一条边当前图是否存在环路,如果存在环路则输出该边.
        """


def test_0():
    s = Solution()
    l1 = [[1,2], [1,3], [2,3]]
    l2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    assert s.findRedundantConnection(l1) == [2, 3]
    assert s.findRedundantConnection(l2) == [1, 4]
