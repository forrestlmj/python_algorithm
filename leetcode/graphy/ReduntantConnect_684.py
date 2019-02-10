# https://leetcode.com/problems/redundant-connection/
import collections
class Solution:
    def isContainCycle(self,graphy,edge):
        stack = list()
        seen = collections.defaultdict(list)
        stack.append(edge[1])
        while len(stack) > 0:
            # 如果存在xun
            current_node = stack.pop()
            if seen[current_node] == True:
                return True
            else:
                seen[current_node] = True
            for i in graphy[current_node]:
                if seen[i]:
                    pass
                else:
                    stack.append(i)
        return False

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        The size of the input 2D-array will be between 3 and 1000.
        Every integer represented in the 2D-array will be between 1 and N,
        where N is the size of the input array.
        切换思路使用DFS,在无向图中不涉及到加权图中的权重因此不需要使用列表数据结构进行排序
        """
        # 使用collection构建集合容器
        # https://docs.python.org/2/library/collections.html
        graphy = collections.defaultdict(set)
        for u, v in edges:
            graphy[u].add(v)
            graphy[v].add(u)
            if self.isContainCycle(graphy, [u, v]):

                return [u, v]




def test_0():
    s = Solution()
    l1 = [[1,2], [1,3], [2,3]]
    l2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    # assert s.findRedundantConnection(l1) == [2, 3]
    assert s.findRedundantConnection(l2) == [1, 4]
def test_205658076():
    s = Solution()
    # 三角形
    l1 = [[1,4],[3,4],[1,3],[1,2],[4,5]]
    # 环路
    l2 = [[1,2],[2,3],[3,4],[1,5],[1,4]]
    # TODO 修改思路为判断当前图中是否存在环路(三角形,多边形),也就是矩阵中u,v
    assert s.findRedundantConnection(l1) == [1, 3]
    assert s.findRedundantConnection(l2) == [1, 4]
    #https://leetcode.com/submissions/detail/205658076/
def test_205830203():
    # https://leetcode.com/submissions/detail/205830203/
    l1 = [[3,4],[1,2],[2,4],[3,5],[2,5]]
    s = Solution()
    assert s.findRedundantConnection(l1) == [2,5]
test_0()
test_205658076()
test_205830203()