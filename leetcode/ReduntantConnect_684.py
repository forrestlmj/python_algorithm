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
        在做图和树的题目时候一定注意边数与点数的关系!
        使用邻接矩阵进行运算:
        """
        N = [[0 for j in range(len(edges)+1)] for i in range(len(edges)+1)]
        for u, v in edges:
            # print(u, v)
            N[u][v] = 1
            count = 0
            for i in N:
                count += i[v]

                if count>1:
                    return [u,v]

def test_0():
    s = Solution()
    l1 = [[1,2], [1,3], [2,3]]
    l2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    assert s.findRedundantConnection(l1) == [2, 3]
    assert s.findRedundantConnection(l2) == [1, 4]
def test_205658076():
    s = Solution()
    l1 = [[1,4],[3,4],[1,3],[1,2],[4,5]]
    # TODO 修改思路为判断当前图中是否存在环路(三角形,多边形),也就是矩阵中u,v
    assert s.findRedundantConnection(l1) == [1, 3]

    #https://leetcode.com/submissions/detail/205658076/
# test_0()
test_205658076()