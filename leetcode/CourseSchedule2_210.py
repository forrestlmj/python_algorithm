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
        if len(prerequisites) == 0:
            return [0]
        a_list = collections.defaultdict(set)
        order = list()
        # order = [0 for i in range(numCourses+1)]
        for edge in prerequisites:
            a_list[edge[1]].add(edge[0])
        c = "xx"
        query = list()
        if len(a_list) == 0 and not "0" in a_list.keys():
            return []
        query.insert(0, 0)
        order.append(0)
        while len(query) > 0:
            # 出队列记录:
            current_course = query.pop()
            # 如果当前课程没有下一课程,则下一步
            if not current_course in a_list.keys():
                pass
            else:
                for next_cource in a_list.get(current_course):
                # 入队列的条件:
                    if order.count(next_cource) == 0:
                        query.insert(0,next_cource)
                        order.append(next_cource)

                    else:
                        pass
        if order.count(numCourses-1) == 0:
            return []
        else:
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
    assert s.findOrder(n, p) == []

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
    assert s.findOrder(n,p) == [1,0]

if __name__ == "__main__":
    test_0()
    test_206484393()
    # test_206485469()

