#https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/
class Solution(object):
    def isDulication(self,l):
        seen = set()
        for i in l:
            if i != '.':
                if i not in seen:
                    seen.add(i)
                else:
                    return True
            else:
                pass
        return False
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            l = list()
            for j in range(len(board[i])):
                l.append(board[i][j])
            if self.isDulication(l):
                return False
        for i in range(9):
            l = list()
            for j in range(9):
                l.append(board[j][i])
            if self.isDulication(l):
                return False
        for i in range(9):
            l = list()
            for j in range(9):
                l.append(board[j][i])
            if self.isDulication(l):
                return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                l = list()
                for s in range(3):
                    for q in range(3):
                        l.append(board[i+s][j+q])
                a =1
                if self.isDulication(l):
                    return False
        return True
def test():
    s = Solution()
    assert s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) ==True

    assert s.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) ==False
    assert s.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]) ==False
if __name__ == "__main__":
    test()