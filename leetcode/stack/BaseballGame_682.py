# https://leetcode.com/problems/baseball-game/
class Solution(object):
    def is_int(self,str):
        try:
            int(str)
            return True
        except:
            return False
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = list()
        for i in ops:
            if self.is_int(i):
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                current = stack[-1]*2
                stack.append(current)
            elif i == "+":
                stack.append(stack[-2]+stack[-1])

        return sum(stack)
def test_0():
    ops = ["5","2","C","D","+"]
    s = Solution()
    assert s.calPoints(ops) == 30
    ops = ["5","-2","4","C","D","9","+","+"]
    s = Solution()
    assert s.calPoints(ops) == 27
    s.calPoints(ops)
if __name__ == "__main__":
    test_0()