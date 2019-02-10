# https://leetcode.com/problems/course-schedule-ii/
# 拓扑图的应用
# 队列和广度优先搜索
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        pre_limit = prerequisites
        a_list = collections.defaultdict(set)
        order = list()
        for edge in prerequisites:
            a_list[edge[1]].add(edge[0])
        query = list()
        while len(pre_limit) > 0:
            query.insert(0, pre_limit[0][1])
            while len(query) > 0:
                # 出队列记录:
                current_course = query.pop()
                order.append(current_course)

                if not current_course in a_list.keys():
                    pass
                else:
                    for next_cource in a_list.get(current_course):
                        # 入队列的条件:
                        pre_limit.remove([next_cource, current_course])

                        if order.count(next_cource) > 0:
                            print("cicyle")
                            return []

                        elif query.count(next_cource) == 0:
                            query.insert(0, next_cource)
                        else:
                            pass


        for i in range(numCourses):
            if i not in order:
                order.append(i)
        return order




def test_0():
    n = 2
    p = [[1, 0]]
    s = Solution()
    assert s.findOrder(n, p) == [0, 1]
    n = 4
    p = [[1, 0], [2, 0], [3, 1], [3, 2]]
    s = Solution()
    assert s.findOrder(n, p) == [0, 1, 2, 3]
    n = 6
    p = [[1,0],[2,0],[3,2],[3,1],[5,4]]
    assert s.findOrder(n, p) == [0,1,2,3,4,5]

def test_206484393():
    # https://leetcode.com/submissions/detail/206484393/
    n = 2
    p = [[1,0]]
    s = Solution()
    assert s.findOrder(n,p) == [0,1]
    n = 1
    p = []
    s = Solution()
    assert s.findOrder(n,p) == [0]
def test_206485469():
    # https://leetcode.com/submissions/detail/206485469/
    n = 2
    p = []
    s = Solution()
    assert s.findOrder(n,p) == [0,1]

def test_1():
    # 重新理解了这道题:这道题潜在意思不是遍历所给的边,获取遍历顺序达到最后一门课程,而是:
    # 一共有N门课程,中间的课程顺序有限制关系,如果没有限制关系,说明课程都要上,不需要排序,
    n = 5
    p = [[1, 0], [0,1]]
    s = Solution()
    # assert s.findOrder(n,p) == []
    n = 7
    p = [[1, 0], [3, 2], [4, 2], [5,3]]
    assert s.findOrder(n,p) == [0,1,2,3,4,5,6]

def test_206855140():
    # https://leetcode.com/submissions/detail/206855140/
    n = 3
    p = [[2,0],[2,1]]
    s = Solution()
    assert s.findOrder(n,p) == [1,0,2]
if __name__ == "__main__":
    test_0()
    test_1()
    test_206484393()

    test_206485469()

