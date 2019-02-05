# https://leetcode.com/problems/redundant-connection-ii/
import collections
class Solution:
    # def isContainCycle(self,graphy,edge):
    #     stack = list()
    #     seen = collections.defaultdict(list)
    #     stack.append(edge[1])
    #     while len(stack) > 0:
    #         # 如果存在xun
    #         current_node = stack.pop()
    #         if seen[current_node] == True:
    #             return True
    #         else:
    #             seen[current_node] = True
    #         for i in graphy[current_node]:
    #             if seen[i]:
    #                 pass
    #             else:
    #                 stack.append(i)
    #     return False

    def findRedundantDirectedConnection(self, edges):
        # 邻接表这里应该是需要一个顺序的,因此应该用list
        graphy = collections.defaultdict(list)

        for u,v in edges:
            graphy[u].append(v)


        seen = [False for i in range(len(edges)+1)]
        stack = list()
        # 从第一个节点开始遍历
        stack.append(edges[0][0])
        while len(stack) > 0:
            current_node = stack.pop()
            seen[current_node] = True
            # 是否已经
            for next_node in graphy[current_node]:
                if seen[next_node] == False:
                    stack.append(next_node)
                else:
                    return [current_node,next_node]

def test_0():
    s = Solution()
    t1 = [[1,2], [1,3], [2,3]]
    assert s.findRedundantDirectedConnection(t1) == [2,3]
    t2 = [[1,2], [2,3], [3,4], [4,1], [1,5]]
    assert s.findRedundantDirectedConnection(t2) == [4,1]
def test_1():
    s = Solution()

    t1 = [[1,2], [2,3], [1,3]]
    assert s.findRedundantDirectedConnection(t1) == [1,3]

if __name__ == "__main__":
    test_0()
    # test_1()