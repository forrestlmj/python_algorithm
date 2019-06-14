# -*- coding: UTF-8 -*-
# 思路，visited矩阵表示是否访问过，从grid[0][0]开始，向右下扩展，当队列交替出现一次全部为0，或1的时候，证明遇到了一个孤岛
class Solution(object):
    def __init__(self):
        self.queue = list()
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # TODO 注意学习列表生成法中 *的使用
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for line in range(grid):
            for j in line:
                if visited
        return 1
def test_0():
    s = Solution()
    s1 = [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]]

    assert s.numIslands(s1) == 1
    s2 = [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]
    assert s.numIslands(s2) == 3
if __name__ == "__main__":
    test_0()